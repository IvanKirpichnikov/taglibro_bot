from dataclasses import dataclass
from typing import dataclass_transform

from taglibro_bot.secret_string import SecretString


@dataclass_transform(frozen_default=True)
def configuration[ClsT](cls: type[ClsT]) -> type[ClsT]:
    return dataclass(frozen=True, slots=True, repr=False)(cls)


@configuration
class DatabaseConfiguration:
    url: SecretString


@configuration
class MeshAccessTokenFernetCryptographerConfiguration:
    key: SecretString


@configuration
class Configuration:
    database: DatabaseConfiguration
    mesh_access_token_fernet_cryptographer: MeshAccessTokenFernetCryptographerConfiguration
