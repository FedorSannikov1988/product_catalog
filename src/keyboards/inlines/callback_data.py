from aiogram.filters.callback_data import CallbackData


class ForDeleteMesage(CallbackData,
                      prefix="delete_mesage"):
    pass


class BackGetManufacturers(CallbackData,
                           prefix="back_get_category_device"):
    pass


class BackGetNameDevices(CallbackData,
                         prefix="back_name_devices"):
    device_category: str


class BackGetNameInformationPictureDevices(CallbackData,
                                           prefix=
                                           "back_devices_name_and_picture"):
    device_category: str


class SelectDeviceCategory(CallbackData,
                           prefix="device_category"):
    device_category: str


class SelectManufacturers(CallbackData,
                          prefix="manufacturers"):
    manufacturer: str


class SelectNameDevices(CallbackData,
                        prefix="name_device"):
    name_device: str


class BackGetManufacturersFromGalleryDevices(CallbackData,
                                             prefix="back_gallery_devices"):
    pass


class GetGalleryDevices(CallbackData,
                        prefix="start_gallery_devices"):
    pass


class ActionGalleryDevices(CallbackData,
                           prefix="action_gallery_devices"):
    turn: str
    pin_message: str
    index_see_name_device: int
