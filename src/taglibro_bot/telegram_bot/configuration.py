from collections.abc import Mapping
from pathlib import Path
from tomllib import loads

from adaptix import Retort, loader

from taglibro_bot.common.configuration import Configuration as BaseConfiguration, configuration
from taglibro_bot.secret_string import SecretString


@configuration
class TelegramBotConfiguration:
    token: SecretString
    redis_url: SecretString


@configuration
class LocalizationConfiguration:
    map: Mapping[str, Path]
    default_language: str


@configuration
class Configuration(BaseConfiguration):
    telegram_bot: TelegramBotConfiguration
    localization: LocalizationConfiguration


retort = Retort(
    recipe=[
        loader(SecretString, SecretString),
    ]
)


def parse_configuration(path: Path) -> Configuration:
    with path.open("r", encoding="utf-8") as config:
        data = loads(config.read())

    return retort.load(data, Configuration)
