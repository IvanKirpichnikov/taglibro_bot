from abc import abstractmethod
from typing import Protocol


class IdentityProvider[EntityT](Protocol):
    @abstractmethod
    async def get(self) -> EntityT:
        raise NotImplementedError
