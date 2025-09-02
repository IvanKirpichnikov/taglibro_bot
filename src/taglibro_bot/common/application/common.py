from dataclasses import dataclass
from typing import dataclass_transform


@dataclass_transform(frozen_default=True)
def interactor[_ClsT](cls: type[_ClsT]) -> type[_ClsT]:
    return dataclass(frozen=True, slots=True)(cls)
