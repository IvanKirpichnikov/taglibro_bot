from collections.abc import Mapping
from typing import Any, override
from uuid import UUID

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncConnection

from taglibro_bot.common.adapters.database.tables import user_table
from taglibro_bot.common.application.user.data_mapper import UserDataMapper
from taglibro_bot.common.domain.user.entity import User, UserId


class UserDataMapperImpl(UserDataMapper):
    __slots__ = ("_connection",)

    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self._connection = connection

    @override
    async def add(self, user: User) -> None:
        statement = insert(user_table).values(
            id=user.id,
            created_at=user.created_at,
        )

        await self._connection.execute(statement)

    def _mapping(self, row: Mapping[Any, Any]) -> User:
        return User(
            id=UserId(UUID(row["id"])),
            created_at=row["created_at"],
        )
