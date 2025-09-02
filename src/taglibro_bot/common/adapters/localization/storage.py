from collections.abc import Mapping
from pathlib import Path
from typing import Any

from fluent.runtime import FluentLocalization, FluentResourceLoader

from taglibro_bot.common.adapters.localization.localization import Localization



class LocalizationStorage:
    __slots__ = (
        "_default_language",
        "_locales",
    )

    def __init__(
        self,
        locales: Mapping[str, Localization],
        default_language: str,
    ) -> None:
        self._locales = locales
        self._default_language = default_language

    def get(self, language: Any) -> Localization:
        try:
            return self._locales[language]
        except KeyError:
            return self._locales[self._default_language]


def localization_storage(
    localizaiton_path_map: Mapping[str, Path],
    default_language: str,
) -> LocalizationStorage:
    locales = {}
    for language, path in localizaiton_path_map.items():
        locales[language] = Localization(
            FluentLocalization(
                locales=[language],
                resource_loader=FluentResourceLoader(roots=[str(path)]),
                resource_ids=[file.name for file in path.iterdir() if file.name.endswith(".ftl")],
            ),
        )

    return LocalizationStorage(
        locales=locales,
        default_language=default_language,
    )
