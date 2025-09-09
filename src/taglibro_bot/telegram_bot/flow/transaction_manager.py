from aiogram_dialog import DialogManager, ShowMode, StartMode

from taglibro_bot.telegram_bot.flow.states import UserFlow


class TransactionManager:
    __slots__ = ("_dialog_manager",)

    def __init__(self, dialog_manager: DialogManager) -> None:
        self._dialog_manager = dialog_manager

    async def user_main_menu(self) -> None:
        await self._dialog_manager.start(
            state=UserFlow.main_menu.menu,
            mode=StartMode.RESET_STACK,
            show_mode=ShowMode.DELETE_AND_SEND,
        )
