from abc import abstractmethod
from typing import Protocol


class IdentityProvider[_EntityT](Protocol):
    @abstractmethod
    async def get(self) -> _EntityT:
        raise NotImplementedError
