from typing import Protocol

from taglibro_bot.telegram_bot.domain.tg_user.entity import OriginTgChatId, OriginTgUserId


class TelegramUser(Protocol):
    @property
    def id(self) -> OriginTgUserId:
        raise NotImplementedError

    @property
    def username(self) -> str | None:
        raise NotImplementedError


class TelegramChat(Protocol):
    @property
    def id(self) -> OriginTgChatId:
        raise NotImplementedError
