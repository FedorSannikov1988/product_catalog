"""
Callback necessary for keyboard.
"""
from aiogram.filters.callback_data import CallbackData


class ForDeleteMessage(CallbackData,
                       prefix="delete_mesage"):
    """
    Callback for delete message and reset FSMstate.
    """
    pass


class BackGetManufacturers(CallbackData,
                           prefix="back_get_category_device"):
    """
    Callback for back choice device category from choice manufacturers.
    """
    pass


class BackGetNameDevices(CallbackData,
                         prefix="back_name_devices"):
    """
    Callback for back choice manufacturers from name devices.
    """
    device_category: str


class BackGetNameInformationPictureDevices(CallbackData,
                                           prefix=
                                           "back_devices_name_and_picture"):
    """
    Callback for back choice manufacturers from
    informatio about name device, picture
    """
    device_category: str


class SelectDeviceCategory(CallbackData,
                           prefix="device_category"):
    """
    Callback for choice device category
    """
    device_category: str


class SelectManufacturers(CallbackData,
                          prefix="manufacturers"):
    """
    Callback for choice manufacturers
    """
    manufacturer: str


class SelectNameDevices(CallbackData,
                        prefix="name_device"):
    """
    Callback for select name devices
    """
    name_device: str


class BackGetManufacturersFromGalleryDevices(CallbackData,
                                             prefix="back_gallery_devices"):
    """
    Back device category from gallery devices
    """
    pass


class GetGalleryDevices(CallbackData,
                        prefix="start_gallery_devices"):
    """
    Callback for start gallery devices.
    """
    pass


class ActionGalleryDevices(CallbackData,
                           prefix="action_gallery_devices"):
    """
    Callback for action gallery devices: right, left, pin.
    """
    turn: str
    pin_message: str
    index_see_name_device: int
