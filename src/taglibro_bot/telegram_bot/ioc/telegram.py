from typing import cast

from dishka import BaseScope, Provider, Scope, provide
from dishka.integrations.aiogram import AiogramMiddlewareData

from taglibro_bot.telegram_bot.adapters.type_hints import TelegramChat, TelegramUser
from taglibro_bot.telegram_bot.flow.transaction_manager import TransactionManager


class TelegramProvider(Provider):
    scope: BaseScope | None = Scope.REQUEST

    @provide
    def telegram_user(self, middleware_data: AiogramMiddlewareData) -> TelegramUser:
        return cast(TelegramUser, middleware_data["event_from_user"])

    @provide
    def telegram_chat(self, middleware_data: AiogramMiddlewareData) -> TelegramChat:
        return cast(TelegramChat, middleware_data["event_chat"])

    @provide
    def transaction_manager(self, middleware_data: AiogramMiddlewareData) -> TransactionManager:
        return TransactionManager(middleware_data["dialog_manager"])
