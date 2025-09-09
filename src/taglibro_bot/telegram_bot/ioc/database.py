from dishka import BaseScope, Provider, Scope, WithParents, provide_all

from taglibro_bot.telegram_bot.adapters.database.tg_user import TgUserDataMapperImpl


class DatabaseProvider(Provider):
    scope: BaseScope | None = Scope.REQUEST

    data_mappers = provide_all(
        WithParents[TgUserDataMapperImpl],
    )
