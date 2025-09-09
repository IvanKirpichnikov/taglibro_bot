from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import Dialog, Window
from dishka import FromDishka

from taglibro_bot.telegram_bot.flow.router_registry import RouterRegistry
from taglibro_bot.telegram_bot.flow.states import UserFlow
from taglibro_bot.telegram_bot.flow.transaction_manager import TransactionManager
from taglibro_bot.telegram_bot.flow.widgets.localization import LocalizationText

router = Router()


@router.message(CommandStart())
async def start(
    event: Message,
    transaction_manager: FromDishka[TransactionManager],
) -> None:
    await transaction_manager.user_main_menu()


dialog = Dialog(
    Window(
        LocalizationText("user-flow-main-menu"),
        state=UserFlow.main_menu.menu,
    ),
)

router_registry = RouterRegistry(dialog, router)
