from typing import override

from taglibro_bot.common.application.idientity_provider import IdentityProvider
from taglibro_bot.common.domain.user.entity import User
from taglibro_bot.telegram_bot.application.tg_user.data_mapper import TgUserDataMapper
from taglibro_bot.telegram_bot.domain.tg_user.entity import OriginTgUserId, TgUser


class UserIdentityProvider(IdentityProvider[User]):
    __slots__ = ("_tg_user_id", "_data_mapper")

    def __init__(
        self,
        tg_user_id: OriginTgUserId,
        data_mapper: TgUserDataMapper,
    ) -> None:
        self._tg_user_id = tg_user_id
        self._data_mapper = data_mapper

    @override
    async def get(self) -> User:
        tg_user = await self._data_mapper.load(self._tg_user_id)
        return tg_user.user


class TgUserIdentityProvider(IdentityProvider[TgUser]):
    __slots__ = ("_tg_user_id", "_data_mapper")

    def __init__(
        self,
        tg_user_id: OriginTgUserId,
        data_mapper: TgUserDataMapper,
    ) -> None:
        self._tg_user_id = tg_user_id
        self._data_mapper = data_mapper

    @override
    async def get(self) -> TgUser:
        tg_user = await self._data_mapper.load(self._tg_user_id)
        return tg_user
