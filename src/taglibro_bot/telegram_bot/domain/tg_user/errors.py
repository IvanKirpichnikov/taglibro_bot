from typing import override

from taglibro_bot.common.domain.errors import DomainError, error
from taglibro_bot.telegram_bot.domain.tg_user.entity import OriginTgUserId


@error
class TgUserLoadError(DomainError):
    tg_user_id: OriginTgUserId

    @override
    def __str__(self) -> str:
        return f"Telegram user load by tg_user_id={self.tg_user_id} error"
