from taglibro_bot.domain.common.errors import DomainError, error
from taglibro_bot.domain.tg_user.entity import OriginTgUserId


@error
class TgUserLoadError(DomainError):
    tg_user_id: OriginTgUserId

    def __str__(self) -> str:
        return f"Telegram user load by tg_user_id={self.tg_user_id} error"
