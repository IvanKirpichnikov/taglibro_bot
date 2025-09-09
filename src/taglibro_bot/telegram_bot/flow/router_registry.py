from collections.abc import Sequence

from aiogram import Router
from aiogram_dialog import Dialog


class RouterRegistry:
    __slots__ = ("_collect_routers",)

    _collect_routers: Sequence[Router]

    def __init__(self, *objs: "Router | RouterRegistry") -> None:
        collect_routers: Sequence[Router] = ()
        for obj in objs:
            if isinstance(obj, RouterRegistry):
                collect_routers = (
                    *collect_routers,
                    *obj._collect_routers,  # noqa: SLF001
                )
            else:
                collect_routers = (*collect_routers, obj)

        self._collect_routers = collect_routers

    def self_include(self, router: Router) -> None:
        if not self._collect_routers:
            return

        router.include_routers(
            *sorted(
                self._collect_routers,
                key=lambda collect_router: not isinstance(collect_router, Dialog),
            )
        )
