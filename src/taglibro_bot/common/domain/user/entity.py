from datetime import UTC, datetime
from typing import NewType
from uuid import UUID

from uuid_utils.compat import uuid7

from taglibro_bot.common.domain.entity import BaseEntity, entity

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
