from collections.abc import Hashable
from dataclasses import dataclass
from typing import Any, dataclass_transform, override
from uuid import UUID


@dataclass_transform(frozen_default=True)
def entity[ClsT](cls: type[ClsT]) -> type[ClsT]:
    return dataclass(frozen=True, slots=True)(cls)


@entity
class BaseEntity[IdT: UUID](Hashable):
    id: IdT

    @override
    def __eq__(self, other: object) -> Any:
        if isinstance(other, BaseEntity):
            return self.id == other.id
        return NotImplemented

    @override
    def __hash__(self) -> int:
        return hash(self.id)
