"""
All keyboards for users .
"""
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .callback_data import BackGetManufacturersFromGalleryDevices, \
                           BackGetNameInformationPictureDevices, \
                           BackGetManufacturers, \
                           BackGetNameDevices, \
                           SelectDeviceCategory, \
                           SelectManufacturers, \
                           SelectNameDevices, \
                           ForDeleteMessage, \
                           GetGalleryDevices, \
                           ActionGalleryDevices


def get_device_category_keyboard(names_for_buttons: list[str]):
    """
    Keyboard for selecting the device category.

    :param names_for_buttons: list[str]
    :return: InlineKeyboardMarkup
    """
    builder = InlineKeyboardBuilder()
    builder_for_complete = InlineKeyboardBuilder()

    for name_one_button in names_for_buttons:
        builder.button(
            text=name_one_button,
            callback_data=
            SelectDeviceCategory(device_category=
                                 name_one_button)
        )

    builder.adjust(2)

    builder_for_complete.button(
        text='Завершить',
        callback_data=
        ForDeleteMessage(delete_mesage=
                        'delete_mesage')
    )

    builder.attach(builder_for_complete)

    return builder.as_markup()


def get_manufacturers_keyboard(names_for_buttons: list[str]):
    """
    Keyboard for selecting the device
    manufacturer.

    :param names_for_buttons: list[str]
    :return: InlineKeyboardMarkup
    """
    builder = InlineKeyboardBuilder()
    builder_for_back = InlineKeyboardBuilder()

    for name_one_button in names_for_buttons:
        builder.button(
            text=name_one_button,
            callback_data=
            SelectManufacturers(manufacturer=
                                name_one_button)
        )

    builder.adjust(2)

    builder_for_back.button(
        text='← Назад',
        callback_data=
        BackGetManufacturers()
    )

    builder.attach(builder_for_back)

    return builder.as_markup()


def get_name_devices_keyboard(device_category: str, names_for_buttons: list[str]):
    """
    Keyboards for selecting the device model.

    :param device_category:
    :param names_for_buttons:
    :return: InlineKeyboardMarkup
    """
    builder = InlineKeyboardBuilder()
    builder_for_back = InlineKeyboardBuilder()

    for name_one_button in names_for_buttons:
        builder.button(
            text=name_one_button,
            callback_data=
            SelectNameDevices(name_device=
                              name_one_button)
        )

    builder.button(
        text='Все устройства',
        callback_data=GetGalleryDevices()
    )

    builder.adjust(2)

    builder_for_back.button(
        text='← Назад',
        callback_data=
        BackGetNameDevices(device_category=
                           device_category)
    )

    builder.attach(builder_for_back)

    return builder.as_markup()


def get_name_information_picture_devices_keyboard(device_category: str,
                                                  names_for_buttons: list[str]):
    """
    Keyboard for displaying information
    (picture and characteristics) about
    the device.

    :param device_category: str
    :param names_for_buttons: list[str]
    :return: InlineKeyboardMarkup
    """

    builder = InlineKeyboardBuilder()
    builder_for_back = InlineKeyboardBuilder()

    for name_one_button in names_for_buttons:
        builder.button(
            text=name_one_button,
            callback_data=
            SelectNameDevices(name_device=
                              name_one_button)
        )

    builder.button(
        text='Все устройства',
        callback_data=
        GetGalleryDevices()
    )

    builder.adjust(2)

    builder_for_back.button(
        text='← Назад',
        callback_data=
        BackGetNameInformationPictureDevices(device_category=
                                             device_category)
    )

    builder.attach(builder_for_back)

    return builder.as_markup()


def for_gallery_devices(index_selected_devices: int):
    """
    Keyboard for shopping gallery .

    :param index_selected_devices: int
    :return: InlineKeyboardMarkup
    """

    line_one = InlineKeyboardBuilder()
    line_two = InlineKeyboardBuilder()

    line_one.button(
        text='←',
        callback_data=
        ActionGalleryDevices(turn='left',
                             pin_message='',
                             index_see_name_device=
                             index_selected_devices)
    )

    line_one.button(
        text='Закрепить',
        callback_data=
        ActionGalleryDevices(turn='',
                             pin_message='pin it',
                             index_see_name_device=
                             index_selected_devices)
    )

    line_one.button(
        text='→',
        callback_data=
        ActionGalleryDevices(turn='right',
                             pin_message='',
                             index_see_name_device=
                             index_selected_devices)
    )
    line_one.adjust(3)

    line_two.button(
        text='В каталог',
        callback_data=
        BackGetManufacturersFromGalleryDevices()
    )

    line_two.button(
        text='Завершить',
        callback_data=ForDeleteMessage()
    )

    line_two.adjust(2)

    line_one.attach(line_two)

    return line_one.as_markup()
