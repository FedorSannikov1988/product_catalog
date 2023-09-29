from aiogram.fsm.state import StatesGroup, State


class DeliveryState(StatesGroup):
    waiting_name_devices = State()
