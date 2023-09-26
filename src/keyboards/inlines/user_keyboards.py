from aiogram.utils.keyboard import InlineKeyboardBuilder
from .callback_data import SelectDeviceCategory, \
                           SelectManufacturers


def get_device_category_keyboard(names_for_buttons: list[str]):
    builder = InlineKeyboardBuilder()

    for name_one_button in names_for_buttons:
        builder.button(
            text=name_one_button,
            callback_data=
            SelectDeviceCategory(device_category=
                                 name_one_button)
        )

    builder.adjust(2)
    return builder.as_markup()


def get_manufacturers_keyboard(device_category: str, names_for_buttons: list[str]):
    builder = InlineKeyboardBuilder()

    for name_one_button in names_for_buttons:
        builder.button(
            text=name_one_button,
            callback_data=
            SelectManufacturers(device_category=device_category,
                                manufacturer=name_one_button)
        )

    builder.adjust(2)
    return builder.as_markup()
