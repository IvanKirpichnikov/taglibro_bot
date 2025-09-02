from taglibro_bot.common.application.atomicity_management import AtomicityManagement
from taglibro_bot.common.application.common import interactor
from taglibro_bot.common.application.idientity_provider import IdentityProvider
from taglibro_bot.common.application.mesh_account.data_mapper import MeshAccountDataMapper
from taglibro_bot.common.domain.mesh_account.entity import MeshAccount, MeshAccountId
from taglibro_bot.common.domain.user.entity import User
from taglibro_bot.secret_string import SecretString


@interactor
class AddMeshAccountInteractor:
    data_mapper: MeshAccountDataMapper
    identity_provider: IdentityProvider[User]
    atomicity_management: AtomicityManagement

    async def execute(self, access_token: SecretString) -> MeshAccountId:
        user = await self.identity_provider.get()

        mesh_account = MeshAccount.factory(user=user, access_token=access_token)
        await self.data_mapper.add(mesh_account)

        await self.atomicity_management.commit()

        return mesh_account.id
