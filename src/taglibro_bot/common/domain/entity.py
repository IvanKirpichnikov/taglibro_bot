from dataclasses import dataclass
from typing import dataclass_transform

from uuid_utils import UUID


@dataclass_transform(frozen_default=True)
def entity[_ClsT](cls: type[_ClsT]) -> type[_ClsT]:
    return dataclass(frozen=True, slots=True)(cls)

@entity
class BaseEntity[_IdT: UUID]:
    id: _IdT

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BaseEntity):
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)
