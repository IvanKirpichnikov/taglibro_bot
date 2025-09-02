from datetime import UTC, datetime
from typing import NewType
from uuid_utils import UUID, uuid7

from taglibro_bot.common.domain.entity import entity
from taglibro_bot.common.domain.user.entity import User

TgUserId = NewType("TgUserId", UUID)
OriginTgUserId = NewType("OriginTgUserId", UUID)
OriginTgChatId = NewType("OriginTgChatId", int)


@entity
class TgUser:
    id: TgUserId
    user: User
    full_name: str
    tg_user_id: OriginTgUserId
    tg_chat_id: OriginTgChatId
    created_at: datetime

    @classmethod
    def factory(
        cls,
        user: User,
        full_name: str,
        tg_user_id: OriginTgUserId,
        tg_chat_id: OriginTgChatId,
    ) -> "TgUser":
        return TgUser(
            id=TgUserId(uuid7()),
            user=user,
            full_name=full_name,
            tg_user_id=tg_user_id,
            tg_chat_id=tg_chat_id,
            created_at=datetime.now(tz=UTC),
        )

    def replace(
        self,
        full_name: str
    ) -> "TgUser":
        return TgUser(
            id=self.id,
            user=self.user,
            full_name=full_name,
            tg_user_id=self.tg_user_id,
            tg_chat_id=self.tg_chat_id,
            created_at=self.created_at,
        )
