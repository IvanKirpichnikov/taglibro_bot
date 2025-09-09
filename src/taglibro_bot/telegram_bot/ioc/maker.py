from dishka import AsyncContainer, make_async_container
from dishka.integrations.aiogram import AiogramProvider

from taglibro_bot.common.configuration import DatabaseConfiguration, MeshAccessTokenFernetCryptographerConfiguration
from taglibro_bot.common.ioc.concated import common_providers
from taglibro_bot.telegram_bot.configuration import Configuration, LocalizationConfiguration, TelegramBotConfiguration
from taglibro_bot.telegram_bot.ioc.database import DatabaseProvider
from taglibro_bot.telegram_bot.ioc.identity_provider import IdentityProviderProvider
from taglibro_bot.telegram_bot.ioc.localization import LocalizationProvider
from taglibro_bot.telegram_bot.ioc.telegram import TelegramProvider


def make_ioc(
    configuration: Configuration,
) -> AsyncContainer:
    return make_async_container(
        common_providers,
        DatabaseProvider(),
        TelegramProvider(),
        IdentityProviderProvider(),
        AiogramProvider(),
        LocalizationProvider(),
        context={
            DatabaseConfiguration: configuration.database,
            TelegramBotConfiguration: configuration.telegram_bot,
            LocalizationConfiguration: configuration.localization,
            MeshAccessTokenFernetCryptographerConfiguration: configuration.mesh_access_token_fernet_cryptographer,
        },
    )
