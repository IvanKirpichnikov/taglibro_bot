from taglibro_bot.telegram_bot.flow.router_registry import RouterRegistry
from taglibro_bot.telegram_bot.flow.user import start

router_registry = RouterRegistry(
    start.router_registry,
)
