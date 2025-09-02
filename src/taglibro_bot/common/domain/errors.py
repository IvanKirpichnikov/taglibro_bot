from dataclasses import dataclass
from typing import dataclass_transform


@dataclass_transform(
    kw_only_default=True,
    eq_default=False,
)
def error[T](cls: type[T]) -> type[T]:
    return dataclass(
        kw_only=True,
        eq=False,
        repr=False,
        match_args=False,
    )(cls)

@error
class DomainError(Exception):
    pass
