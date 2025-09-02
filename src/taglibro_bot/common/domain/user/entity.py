from datetime import UTC, datetime
from typing import NewType
from uuid_utils import UUID, uuid7

from taglibro_bot.common.domain.entity import entity, BaseEntity


UserId = NewType("UserId", UUID)


@entity
class User(BaseEntity[UserId]):
    created_at: datetime

    @classmethod
    def factory(cls) -> "User":
        return cls(
            id=UserId(uuid7()),
            created_at=datetime.now(tz=UTC),
        )
