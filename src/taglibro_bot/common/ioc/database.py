from collections.abc import AsyncIterable

from dishka import BaseScope, Provider, Scope, WithParents, provide, provide_all
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine, create_async_engine

from taglibro_bot.common.adapters.database.mesh_account import MeshAccountDataMapperImpl
from taglibro_bot.common.adapters.database.user import UserDataMapperImpl
from taglibro_bot.common.configuration import DatabaseConfiguration


class DatabaseProvider(Provider):
    scope: BaseScope | None = Scope.REQUEST

    @provide(scope=Scope.APP)
    async def make_engine(self, configuration: DatabaseConfiguration) -> AsyncIterable[AsyncEngine]:
        engine = create_async_engine(configuration.url.get_value())
        yield engine
        await engine.dispose()

    @provide()
    async def make_connection(self, engine: AsyncEngine) -> AsyncIterable[AsyncConnection]:
        async with engine.connect() as connection:
            yield connection

    data_mappers = provide_all(
        WithParents[UserDataMapperImpl],
        WithParents[MeshAccountDataMapperImpl],
    )
