from abc import abstractmethod
from typing import Protocol

from taglibro_bot.common.domain.mesh_account.entity import MeshAccount
from taglibro_bot.common.domain.user.entity import UserId


class MeshAccountDataMapper(Protocol):
    @abstractmethod
    async def add(self, entity: MeshAccount) -> None:
        raise NotImplementedError

    @abstractmethod
    async def load(self, user_id: UserId) -> MeshAccount:
        raise NotImplementedError

    @abstractmethod
    async def update(self, entity: MeshAccount) -> None:
        raise NotImplementedError
