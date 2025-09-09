from dishka import DEFAULT_COMPONENT, Component
from dishka.provider import BaseProvider


class ConcatProvider(BaseProvider):
    def __init__(
        self,
        *providers: BaseProvider,
        component: Component = DEFAULT_COMPONENT,
    ) -> None:
        super().__init__(component)

        for provider in providers:
            self.factories.extend(provider.factories)
            self.aliases.extend(provider.aliases)
            self.decorators.extend(provider.decorators)
            self.context_vars.extend(provider.context_vars)
