from aiogram.fsm.state import State, StatesGroup

class saqlsh(StatesGroup):
    waiting_for_name = State()
    qidruv = State()
    tarjima = State()
    ism = State()
    tel = State()
    ariza = State()