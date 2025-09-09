from datetime import UTC, datetime
from typing import NewType
from uuid import UUID

from uuid_utils.compat import uuid7

from taglibro_bot.common.domain.entity import BaseEntity, entity
from taglibro_bot.common.domain.user.entity import User
from taglibro_bot.secret_string import SecretString

MeshAccountId = NewType("MeshAccountId", UUID)


@entity
class MeshAccount(BaseEntity[MeshAccountId]):
    user: User
    access_token: SecretString
    created_at: datetime

    @classmethod
    def factory(
        cls,
        user: User,
        access_token: SecretString,
    ) -> "MeshAccount":
        return cls(
            id=MeshAccountId(uuid7()),
            user=user,
            access_token=access_token,
            created_at=datetime.now(tz=UTC),
        )

    def replace(self, access_token: SecretString) -> "MeshAccount":
        return MeshAccount(
            id=self.id,
            user=self.user,
            access_token=access_token,
            created_at=self.created_at,
        )
