from keyboards import get_device_category_keyboard, \
                      get_manufacturers_keyboard, \
                      SelectDeviceCategory, \
                      SelectManufacturers
from middlewares import GetDeviceManufacturer, \
                        GetDeviceCategory
from loader import router_for_catalog, bot
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram import types


router_for_catalog.message.middleware(GetDeviceCategory())
router_for_catalog.callback_query.middleware(GetDeviceManufacturer())


@router_for_catalog.message(Command("catalog"))
async def get_device_category(message: types.Message,
                              all_device_category: list):

    text: str = 'Выберите категорию устройства: \n '

    await message.answer(text=text,
                         reply_markup=
                         get_device_category_keyboard(names_for_buttons=
                                                      all_device_category))


@router_for_catalog.callback_query(SelectDeviceCategory.filter())
async def get_manufacturers(callback: CallbackQuery,
                            callback_data: SelectDeviceCategory,
                            manufacturers: list):

    if not manufacturers:
        await callback.answer(
            text="На данный момент устройств этой категории нет на складе",
            show_alert=False
        )
    else:
        chat_id = callback.message.chat.id
        message_id = callback.message.message_id
        device_category = callback_data.device_category

        print('Категория:')
        print(callback_data.device_category)

        text: str = 'Выберите производителя устройства: \n'

        await bot.edit_message_text(text=text,
                                    chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=
                                    get_manufacturers_keyboard(
                                        device_category=
                                        device_category,
                                        names_for_buttons=
                                        manufacturers))

