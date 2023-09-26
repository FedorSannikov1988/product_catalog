from aiogram.filters.callback_data import CallbackData


class SelectDeviceCategory(CallbackData, prefix="device_category"):
    device_category: str
