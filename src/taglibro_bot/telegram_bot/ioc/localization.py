from dishka import Provider, Scope, provide

from taglibro_bot.telegram_bot.adapters.localization.localization import Localization
from taglibro_bot.telegram_bot.adapters.localization.storage import LocalizationStorage, localization_storage
from taglibro_bot.telegram_bot.configuration import LocalizationConfiguration


class LocalizationProvider(Provider):
    @provide(scope=Scope.APP)
    def localization_storage(
        self,
        configuration: LocalizationConfiguration,
    ) -> LocalizationStorage:
        return localization_storage(
            localizaiton_path_map=configuration.map,
            default_language=configuration.default_language,
        )

    @provide(scope=Scope.REQUEST)
    def localization(self, storage: LocalizationStorage) -> Localization:
        return storage.get("ru")
