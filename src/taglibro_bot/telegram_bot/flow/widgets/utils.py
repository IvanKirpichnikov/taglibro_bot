import typing
from collections.abc import Callable
from typing import Any

from magic_filter import MagicFilter

type _CallableDataGetter = Callable[[dict[str, Any]], dict[str, Any]]
type DataGetter = dict[str, MagicFilter] | MagicFilter | _CallableDataGetter | None


def _magic_filter_map_data_getter(
    magic_filter_map: dict[str, MagicFilter],
) -> _CallableDataGetter:
    def wrapper(data: dict[str, Any]) -> dict[str, Any]:
        result = {key: magic_filter.resolve(data) for key, magic_filter in magic_filter_map.items()}
        return result

    return wrapper


def _magic_filter_data_getter(
    magic_filter: MagicFilter,
) -> _CallableDataGetter:
    def wrapper(data: dict[str, Any]) -> dict[str, Any]:
        result = magic_filter.resolve(data)
        return typing.cast("dict[str, Any]", result)

    return wrapper


def _empty_data_getter(data: dict[str, Any]) -> dict[str, Any]:
    return {}


def prepare_data_getter(data_getter: DataGetter) -> _CallableDataGetter:
    if data_getter is None:
        return _empty_data_getter
    if isinstance(data_getter, MagicFilter):
        return _magic_filter_data_getter(data_getter)
    if isinstance(data_getter, dict):
        return _magic_filter_map_data_getter(data_getter)
    return data_getter
