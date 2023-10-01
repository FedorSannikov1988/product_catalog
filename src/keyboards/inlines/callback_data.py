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


class GalleryDevices(CallbackData,
                     prefix="gallery_devices"):
    names_devices: str


class BackGetManufacturersFromGalleryDevices(CallbackData,
                                             prefix=
                                             "back_gallery_devices"):
    pass
