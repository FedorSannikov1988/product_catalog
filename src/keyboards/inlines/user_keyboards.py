from aiogram.utils.keyboard import InlineKeyboardBuilder
from .callback_data import SelectDeviceCategory, \
                           SelectManufacturers, \
                           SelectNameDevices, \
                           ForDeleteMesage, \
                           ForBack


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

    builder_for_complete = InlineKeyboardBuilder()
    builder_for_complete.button(
        text='Завершит',
        callback_data=
        ForDeleteMesage(delete_mesage=
                        'delete_mesage')
    )

    builder.attach(builder_for_complete)

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

    builder_for_back = InlineKeyboardBuilder()
    builder_for_back.button(
        text='<< Назад',
        callback_data=
        ForBack(back_to='device_category')
    )

    builder.attach(builder_for_back)

    return builder.as_markup()


def get_name_devices_keyboard(manufacturer: str,
                              device_category: str,
                              names_for_buttons: list[str]):
    builder = InlineKeyboardBuilder()

    for name_one_button in names_for_buttons:
        builder.button(
            text=name_one_button,
            callback_data=
            SelectNameDevices(device_category=device_category,
                              manufacturer=manufacturer,
                              name_device=name_one_button))

    builder.adjust(2)
    return builder.as_markup()
