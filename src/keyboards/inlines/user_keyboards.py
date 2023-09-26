from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.inlines.callback_data import SelectDeviceCategory


def get_device_category_keyboard(names_for_buttons: list[str]):
    builder = InlineKeyboardBuilder()

    #buttons = []

    for name_one_button in names_for_buttons:
        builder.button(
            text=name_one_button, callback_data=SelectDeviceCategory(device_category=name_one_button)
        )


        #button = InlineKeyboardButton(text=name_one_button,
        #                              callback_data=SelectDeviceCategory(device_category=name_one_button)
        #                              )
        #buttons.append([button])

    #keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    builder.adjust(2)
    return builder.as_markup()
