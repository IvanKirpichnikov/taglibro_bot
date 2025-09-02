from abc import abstractmethod
from typing import Protocol

from taglibro_bot.telegram_bot.domain.tg_user.entity import OriginTgUserId, TgUser

class TgUserDataMapper(Protocol):
    __slots__ = ()

    @abstractmethod
    async def add(self, entity: TgUser) -> None:
        raise NotImplementedError

    @abstractmethod
    async def load(self, tg_user_id: OriginTgUserId) -> TgUser:
        raise NotImplementedError

    @abstractmethod
    async def update(self, entity: TgUser) -> None:
        raise NotImplementedError
