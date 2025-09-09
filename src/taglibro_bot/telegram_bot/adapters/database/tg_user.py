from collections.abc import Mapping
from typing import Any, override
from uuid import UUID

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncConnection

from taglibro_bot.common.adapters.database.tables import user_table
from taglibro_bot.common.domain.user.entity import User, UserId
from taglibro_bot.telegram_bot.adapters.database.tables import tg_user_table
from taglibro_bot.telegram_bot.application.tg_user.data_mapper import TgUserDataMapper
from taglibro_bot.telegram_bot.domain.tg_user.entity import OriginTgUserId, TgUser, TgUserId


class TgUserDataMapperImpl(TgUserDataMapper):
    __slots__ = ("_connection",)

    def __init__(self, connection: AsyncConnection) -> None:
        self._connection = connection

    @override
    async def add(self, entity: TgUser) -> None:
        statement = insert(tg_user_table).values(
            id=entity.id,
            user_id=entity.user.id,
            created_at=entity.created_at,
            full_name=entity.full_name,
            tg_user_id=entity.tg_user_id,
            tg_chat_id=entity.tg_chat_id,
        )
        await self._connection.execute(statement)

    @override
    async def load(self, tg_user_id: OriginTgUserId) -> TgUser:
        statement = (
            select(tg_user_table)
            .where(tg_user_table.c.tg_user_id == tg_user_id)
            .join(user_table, tg_user_table.c.user_id == user_table.c.id)
        )

        cursor_result = await self._connection.execute(statement)
        fetchone = cursor_result.mappings().fetchone()
        if fetchone is None:
            raise RuntimeError

        return self._mapping(fetchone)

    @override
    async def update(self, entity: TgUser) -> None:
        statement = update(tg_user_table).values(full_name=entity.full_name).where(tg_user_table.c.id == entity.id)
        await self._connection.execute(statement)

    def _mapping(self, row: Mapping[Any, Any]) -> TgUser:
        user = User(
            id=UserId(UUID(row["users.id"])),
            created_at=row["users.created_at"],
        )
        return TgUser(
            id=TgUserId(UUID(row["tg_users.id"])),
            user=user,
            full_name=row["tg_users.full_name"],
            tg_chat_id=row["tg_users.tg_chat_id"],
            tg_user_id=row["tg_users.tg_user_id"],
            created_at=row["tg_users.created_at"],
        )
