from aiogram import Router
from dishka import AsyncContainer
from dishka.integrations.aiogram import ContainerMiddleware, inject_router


def setup_ioc(
    container: AsyncContainer,
    router: Router,
    *,
    auto_inject: bool = False,
) -> None:
    middleware = ContainerMiddleware(container)

    for observer in router.observers.values():
        observer.middleware(middleware)

    if auto_inject:
        callback = lambda: inject_router(router=router)
        router.startup.register(callback)
