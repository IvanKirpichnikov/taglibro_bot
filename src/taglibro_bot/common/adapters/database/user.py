from typing import Any, Mapping
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncConnection
from uuid_utils import UUID

from taglibro_bot.common.application.user.data_mapper import UserDataMapper
from taglibro_bot.common.domain.user.entity import User, UserId
from taglibro_bot.common.adapters.database.tables import user_table


class UserDataMapperImpl(UserDataMapper):
    __slots__ = ("_connection",)

    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self._connection = connection

    async def add(self, user: User) -> User:
        statement = (
            insert(user_table)
            .values(
                id=user.id,
                created_at=user.created_at,
            )
            .returning(user_table)
        )

        cursor_result = await self._connection.execute(statement)

        fetchone = cursor_result.mappings().fetchone()
        if fetchone is None:
            raise RuntimeError

        return self._mapping(fetchone)


    def _mapping(self, row: Mapping[Any, Any]) -> User:
        return User(
            id=UserId(UUID(row["id"])),
            created_at=row["created_at"],
        )
