from aiogram.filters.callback_data import CallbackData


class ForDeleteMesage(CallbackData,
                      prefix="delete_mesage"):
    pass


class BackGetManufacturers(CallbackData,
                           prefix="back_get_category_device"):
    pass


class BackGetNameDevices(CallbackData,
                         prefix="back_get_devices_name"):
    device_category: str


class BackGetNameInformationPictureDevices(CallbackData,
                                           prefix=
                                           "back_get_devices_picture_information_name"):
    device_category: str


class SelectDeviceCategory(CallbackData,
                           prefix="device_category"):
    device_category: str


class SelectManufacturers(CallbackData,
                          prefix="manufacturers"):
    device_category: str
    manufacturer: str


class SelectNameDevices(CallbackData,
                        prefix="name_devices"):
    device_category: str
    manufacturer: str
    name_device: str


class BackGetManufacturersFromGalleryDevices(CallbackData,
                                             prefix="back_gallery_devices"):
    pass


class GetGalleryDevices(CallbackData,
                        prefix="start_gallery_devices"):
    device_category: str
    manufacturer: str


class ActionGalleryDevices(CallbackData,
                           prefix="action_gallery_devices"):
    turn: str
    manufacturer: str
    device_category: str
    see_name_device: str
    pin_message: str
