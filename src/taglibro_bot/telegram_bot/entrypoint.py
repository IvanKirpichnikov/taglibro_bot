import asyncio
import logging
from argparse import ArgumentParser
from pathlib import Path
from typing import Protocol, cast

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from aiogram_dialog import setup_dialogs
from dishka.integrations.aiogram import setup_dishka

from taglibro_bot.telegram_bot.configuration import parse_configuration
from taglibro_bot.telegram_bot.flow.router_registry import RouterRegistry
from taglibro_bot.telegram_bot.flow.user.router_registry import router_registry as user_router_registry
from taglibro_bot.telegram_bot.ioc.maker import make_ioc
from taglibro_bot.telegram_bot.ioc.setup import setup_ioc


class CliArgs(Protocol):
    config_path: Path


def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s.%(funcName)s:%(lineno)d - %(message)s",
    )

    cli_args = parse_cli_args()
    asyncio.run(async_main(cli_args.config_path))


def parse_cli_args() -> CliArgs:
    parser = create_argument_parser()
    cli_args = parser.parse_args()
    return cast(CliArgs, cli_args)


def create_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    bot_sub_parser = subparsers.add_parser("telegram_bot")

    bot_sub_parser.add_argument(
        "--config",
        dest="config_path",
        type=Path,
        help="path to config toml file",
    )

    return parser


async def async_main(config_path: Path) -> None:
    configuration = parse_configuration(config_path)

    ioc = make_ioc(configuration)

    telegram_bot_configuration = configuration.telegram_bot

    bot = Bot(token=telegram_bot_configuration.token.get_value())
    storage = RedisStorage.from_url(
        url=telegram_bot_configuration.redis_url.get_value(),
        key_builder=DefaultKeyBuilder(
            with_bot_id=True,
            with_destiny=True,
        )
    )
    dispatcher = Dispatcher(storage=storage, events_isolation=storage.create_isolation())

    router_registry = RouterRegistry(
        user_router_registry,
    )
    router_registry.self_include(dispatcher)

    setup_dialogs(dispatcher)
    setup_ioc(ioc, dispatcher, auto_inject=True)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    main()
