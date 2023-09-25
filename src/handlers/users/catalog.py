from keyboards import get_device_category_keyboard
from loader import router_for_catalog, db
from aiogram.filters import Command
from aiogram import types


@router_for_catalog.message(Command("catalog"))
async def get_device_category(message: types.Message):
    print(await db.info_all_device_category())
    text: str = 'Выберите категорию устройства: \n '

    await message.answer(text=text, reply_markup=get_device_category_keyboard())