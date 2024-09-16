from aiogram.fsm.state import State, StatesGroup

class Adverts(StatesGroup):
    adverts = State()


class SendState(StatesGroup):
    ask = State()
    time = State()
    confirm = State()
    # send = State()