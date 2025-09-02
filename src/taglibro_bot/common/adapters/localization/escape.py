from enum import Enum
from types import NoneType
from typing import Any, Final
from uuid import UUID

_ESCAPE_STR_TYPES: Final = (
    NoneType,
    bool,
    UUID,
)


def localization_escape(value: Any) -> Any:
    if isinstance(value, _ESCAPE_STR_TYPES):
        return str(value)
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, dict):
        return {key: localization_escape(value) for key, value in value.items()}
    if isinstance(value, list):
        return [localization_escape(_) for _ in value]
    return value
