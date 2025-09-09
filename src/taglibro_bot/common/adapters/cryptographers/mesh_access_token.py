from typing import override

from cryptography.fernet import Fernet

from taglibro_bot.common.application.mesh_account.cryptographer import MeshAccessTokenCryptographer
from taglibro_bot.secret_string import SecretString


class MeshAccessTokenFernetCryptographer(MeshAccessTokenCryptographer):
    __slots__ = ("_fernet",)

    def __init__(self, fernet: Fernet) -> None:
        self._fernet = fernet

    @override
    def crypto(self, access_token: SecretString) -> str:
        encrypted_token = self._fernet.encrypt(access_token.get_value().encode("utf-8"))
        return encrypted_token.decode("utf-8")

    @override
    def decrypto(self, raw_access_token: str) -> SecretString:
        decrypted_token = self._fernet.decrypt(raw_access_token).decode("utf-8")
        return SecretString(decrypted_token)
