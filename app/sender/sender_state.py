from aiogram.fsm.state import State, StatesGroup


class Steps(StatesGroup):
    get_message = State()
