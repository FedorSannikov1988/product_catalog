from aiogram.types import InlineKeyboardMarkup, \
                          InlineKeyboardButton


def get_device_category_keyboard(names_for_buttons: list[str]):
    buttons = []

    for name_one_button in names_for_buttons:
        button = InlineKeyboardButton(text=name_one_button,
                                      callback_data=name_one_button)
        buttons.append([button])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
