from cryptography.fernet import Fernet
from dishka import Provider, Scope, provide

from taglibro_bot.common.adapters.cryptographers.mesh_access_token import MeshAccessTokenFernetCryptographer
from taglibro_bot.common.application.mesh_account.cryptographer import MeshAccessTokenCryptographer
from taglibro_bot.common.configuration import MeshAccessTokenFernetCryptographerConfiguration


class CryptographerProvider(Provider):
    @provide(scope=Scope.APP)
    def make_fernet(
        self,
        configuration: MeshAccessTokenFernetCryptographerConfiguration,
    ) -> Fernet:
        return Fernet(key=configuration.key.get_value())

    @provide(scope=Scope.REQUEST)
    def make_mesh_access_token_cryptographer(
        self,
        fernet: Fernet
    ) -> MeshAccessTokenCryptographer:
        return MeshAccessTokenFernetCryptographer(fernet)
