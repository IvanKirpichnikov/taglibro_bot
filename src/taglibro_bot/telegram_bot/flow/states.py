from aiogram.fsm.state import State, StatesGroup


class _UserMainMenuFlow(StatesGroup):
    menu = State()


class UserFlow(StatesGroup):
    main_menu = _UserMainMenuFlow()
