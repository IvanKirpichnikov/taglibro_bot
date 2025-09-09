from typing import Any, override

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Format
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from taglibro_bot.telegram_bot.adapters.localization.localization import Localization
from taglibro_bot.telegram_bot.flow.widgets.utils import DataGetter, prepare_data_getter


class LocalizationText(Format):
    __slots__ = ("_data_getter",)

    def __init__(
        self,
        text: str,
        data_getter: DataGetter = None,
        when: WhenCondition = None,
    ) -> None:
        super().__init__(text=text, when=when)
        self._data_getter = prepare_data_getter(data_getter)

    @inject
    @override
    async def _render_text(
        self,
        data: dict[str, Any],
        manager: DialogManager,
        localization: FromDishka[Localization],
    ) -> str:
        key = await super()._render_text(data, manager)
        localization_data = self._data_getter(data)
        return localization(key, **localization_data)
