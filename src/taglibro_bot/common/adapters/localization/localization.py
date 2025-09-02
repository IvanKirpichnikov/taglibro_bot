from typing import Any

from fluent.runtime import FluentLocalization

from taglibro_bot.common.adapters.localization.errors import NotFoundLocalizationTextError
from taglibro_bot.common.adapters.localization.escape import localization_escape



class Localization:
    __slots__ = ("_locale",)

    def __init__(self, locale: FluentLocalization) -> None:
        self._locale = locale

    def __call__(self, key: str, /, **kwargs: Any) -> str:
        if kwargs:
            data = localization_escape(kwargs)
        else:
            data = None

        result = self._locale.format_value(key, data)
        if result == key:
            raise NotFoundLocalizationTextError(key=key)
        return result
