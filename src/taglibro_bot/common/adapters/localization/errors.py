from typing import override


class NotFoundLocalizationTextError(Exception):
    def __init__(self, key: str) -> None:
        self._key = key
        super().__init__(key)

    @override
    def __str__(self) -> str:
        return f"Not found localization text by key {self._key!r}"
