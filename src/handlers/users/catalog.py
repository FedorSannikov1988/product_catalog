from aiogram.types import CallbackQuery

from keyboards import get_device_category_keyboard, SelectDeviceCategory

from loader import router_for_catalog, db
from aiogram.filters import Command
from aiogram import types
from aiogram import F


@router_for_catalog.message(Command("catalog"))
async def get_device_category(message: types.Message):

    all_device_category = await db.info_all_device_category()

    names_for_buttons = []
    for one_category in all_device_category:
        names_for_buttons.append(one_category[1])


    text: str = 'Выберите категорию устройства: \n '

    await message.answer(text=text,
                         reply_markup=
                         get_device_category_keyboard(names_for_buttons=
                                                      names_for_buttons))


@router_for_catalog.callback_query(SelectDeviceCategory.filter())
async def check(callback: CallbackQuery,
                callback_data: SelectDeviceCategory):
    print("-----")
    print(callback_data.device_category)
    print("-----")
    print(callback)
    print("-----")
    await callback.answer(
        "Работает",
        show_alert=True
    )


#@router_for_catalog.callback_query(F.data == "Ноутбуки")
#async def checkin_confirm(callback: CallbackQuery):
#    print(callback)
#    await callback.answer(
#        "Спасибо, подтверждено!",
#        show_alert=True
#    )


#@router_for_catalog.callback_query()
#async def checkin_confirm(callback: CallbackQuery):
#    print(callback)
#    await callback.answer(
#        "Спасибо, подтверждено!",
#        show_alert=True
#    )