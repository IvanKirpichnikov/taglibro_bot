from taglibro_bot.common.application.atomicity_management import AtomicityManagement
from taglibro_bot.common.application.common import interactor
from taglibro_bot.common.application.user.data_mapper import UserDataMapper
from taglibro_bot.common.domain.user.entity import User
from taglibro_bot.telegram_bot.application.tg_user.data_mapper import TgUserDataMapper
from taglibro_bot.telegram_bot.domain.tg_user.entity import OriginTgChatId, OriginTgUserId, TgUser
from taglibro_bot.telegram_bot.domain.tg_user.errors import TgUserLoadError


@interactor
class UpsertTgUserInteractor:
    user_data_mapper: UserDataMapper
    tg_user_data_mapper: TgUserDataMapper
    atomicity_management: AtomicityManagement

    async def execute(
        self,
        full_name: str,
        tg_user_id: OriginTgUserId,
        tg_chat_id: OriginTgChatId,
    ) -> None:
        try:
            tg_user = await self.tg_user_data_mapper.load(tg_user_id)
        except TgUserLoadError:
            user = User.factory()
            tg_user = TgUser.factory(
                user=user,
                full_name=full_name,
                tg_chat_id=tg_chat_id,
                tg_user_id=tg_user_id,
            )
            await self.user_data_mapper.add(user)
            await self.tg_user_data_mapper.add(tg_user)
        else:
            tg_user = tg_user.replace(full_name=full_name)
            await self.tg_user_data_mapper.update(tg_user)

        await self.atomicity_management.commit()
