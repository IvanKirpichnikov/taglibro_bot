from collections.abc import Container, Hashable
from typing import Any, Final, Sized


_SECRET_REPR: Final = "*******"


class SecretString(Container[Any], Hashable, Sized):
    __slots__ = ("_value",)

    def __init__(self, value: str) -> None:
        self._value = value

    def __hash__(self) -> int:
        return hash(self._value)

    def __len__(self) -> int:
        return len(self._value)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, str):
            return self._value == value
        return NotImplemented

    def __contains__(self, value: object) -> bool:
        if isinstance(value, str):
            return value in self._value
        return NotImplemented

    def get_value(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return _SECRET_REPR
