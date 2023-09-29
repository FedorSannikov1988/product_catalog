from aiogram.filters.callback_data import CallbackData


class ForDeleteMesage(CallbackData, prefix="delete_mesage"):
    delete_mesage: str


class ForBack(CallbackData, prefix="back"):
    back_to: str


class SelectDeviceCategory(CallbackData, prefix="device_category"):
    device_category: str


class SelectManufacturers(CallbackData, prefix="manufacturers"):
    device_category: str
    manufacturer: str


class SelectNameDevices(CallbackData, prefix="name_devices"):
    device_category: str
    manufacturer: str
    name_device: str


