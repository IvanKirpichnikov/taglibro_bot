from dishka import BaseScope, Provider, Scope, provide

from taglibro_bot.common.application.idientity_provider import IdentityProvider
from taglibro_bot.common.domain.user.entity import User
from taglibro_bot.telegram_bot.adapters.identity_providers import TgUserIdentityProvider, UserIdentityProvider
from taglibro_bot.telegram_bot.adapters.type_hints import TelegramUser
from taglibro_bot.telegram_bot.application.tg_user.data_mapper import TgUserDataMapper
from taglibro_bot.telegram_bot.domain.tg_user.entity import TgUser


class IdentityProviderProvider(Provider):
    scope: BaseScope | None = Scope.REQUEST

    @provide
    def make_user_identity_provider(
        self,
        telegram_user: TelegramUser,
        data_mapper: TgUserDataMapper,
    ) -> IdentityProvider[User]:
        return UserIdentityProvider(
            data_mapper=data_mapper,
            tg_user_id=telegram_user.id,
        )

    @provide
    def make_tg_user_identity_provider(
        self,
        telegram_user: TelegramUser,
        data_mapper: TgUserDataMapper,
    ) -> IdentityProvider[TgUser]:
        return TgUserIdentityProvider(
            data_mapper=data_mapper,
            tg_user_id=telegram_user.id,
        )
