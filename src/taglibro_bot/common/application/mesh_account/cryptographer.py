from abc import abstractmethod

from taglibro_bot.secret_string import SecretString


class MeshAccessTokenCryptographer:
    @abstractmethod
    def crypto(self, access_token: SecretString) -> str:
        raise NotImplementedError

    @abstractmethod
    def decrypto(self, raw_access_token: str) -> SecretString:
        raise NotImplementedError
