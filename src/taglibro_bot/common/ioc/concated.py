from taglibro_bot._internal.dishka import ConcatProvider
from taglibro_bot.common.ioc.cryptographer import CryptographerProvider
from taglibro_bot.common.ioc.database import DatabaseProvider

common_providers = ConcatProvider(
    DatabaseProvider(),
    CryptographerProvider(),
)
