from aiogram.types import InlineKeyboardMarkup, \
                          InlineKeyboardButton


def get_device_category_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="↠", callback_data="num_decr"),
            InlineKeyboardButton(text="+1", callback_data="num_incr")
        ],
        [InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard