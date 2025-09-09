from collections.abc import Mapping
from typing import Any, override
from uuid import UUID

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncConnection

from taglibro_bot.common.adapters.database.tables import mesh_account_table, user_table
from taglibro_bot.common.application.mesh_account.cryptographer import MeshAccessTokenCryptographer
from taglibro_bot.common.application.mesh_account.data_mapper import MeshAccountDataMapper
from taglibro_bot.common.domain.mesh_account.entity import MeshAccount, MeshAccountId
from taglibro_bot.common.domain.user.entity import User, UserId


class MeshAccountDataMapperImpl(MeshAccountDataMapper):
    __slots__ = (
        "_connection",
        "_access_token_cryptographer",
    )

    def __init__(
        self,
        connection: AsyncConnection,
        access_token_cryptographer: MeshAccessTokenCryptographer,
    ) -> None:
        self._connection = connection
        self._access_token_cryptographer = access_token_cryptographer

    @override
    async def add(self, entity: MeshAccount) -> None:
        access_token = self._access_token_cryptographer.crypto(entity.access_token)

        statement = insert(mesh_account_table).values(
            id=entity.id,
            user_id=entity.user.id,
            access_token=access_token,
            created_at=entity.created_at,
        )

        await self._connection.execute(statement)

    @override
    async def load(self, user_id: UserId) -> MeshAccount:
        statement = (
            select(mesh_account_table)
            .where(mesh_account_table.c.user_id == user_id)
            .join(user_table, mesh_account_table.c.user_id == user_table.c.id)
        )

        cursor_result = await self._connection.execute(statement)
        fetchone = cursor_result.mappings().fetchone()
        if fetchone is None:
            raise RuntimeError

        return self._mapping(fetchone)

    @override
    async def update(self, entity: MeshAccount) -> None:
        statement = (
            update(mesh_account_table)
            .values(
                access_token=entity.access_token,
            )
            .where(mesh_account_table.c.id == entity.id)
        )
        await self._connection.execute(statement)

    def _mapping(self, row: Mapping[Any, Any]) -> MeshAccount:
        access_token = self._access_token_cryptographer.decrypto(row["mesh_accounts.access_token"])

        user = User(
            id=UserId(UUID(row["users.id"])),
            created_at=row["users.created_at"],
        )
        return MeshAccount(
            id=MeshAccountId(UUID(row["mesh_accounts.id"])),
            user=user,
            access_token=access_token,
            created_at=row["mesh_accounts.created_at"],
        )
