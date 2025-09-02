from abc import abstractmethod
from typing import Protocol

from taglibro_bot.common.domain.user.entity import User


class UserDataMapper(Protocol):
    @abstractmethod
    async def add(self, user: User) -> User:
        raise NotImplementedError
