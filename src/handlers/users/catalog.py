from keyboards import get_device_category_keyboard, \
                      get_manufacturers_keyboard, \
                      get_name_devices_keyboard, \
                      SelectDeviceCategory, \
                      SelectManufacturers, \
                      SelectNameDevices, \
                      ForDeleteMesage, \
                      ForBack
from middlewares import GetDeviceCategoryStart, \
                        GetDeviceManufacturer, \
                        GetDeviceCategoryBack, \
                        GetDevicesName
from loader import router_for_catalog, bot, db
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, \
                          FSInputFile
from aiogram.filters import Command
from aiogram import types

router_for_catalog.message.middleware(GetDeviceCategoryStart())
router_for_catalog.callback_query.middleware(GetDeviceCategoryBack())
router_for_catalog.callback_query.middleware(GetDeviceManufacturer())
router_for_catalog.callback_query.middleware(GetDevicesName())


@router_for_catalog.message(Command("catalog"))
async def get_device_category(message: types.Message,
                              all_device_category: list):

    text: str = 'Выберите категорию устройства: \n '

    await message.answer(text=text,
                         reply_markup=
                         get_device_category_keyboard(
                             names_for_buttons=
                             all_device_category))


@router_for_catalog.callback_query(ForBack.filter())
async def back_get_device_category(callback: CallbackQuery,
                                   all_device_category: list):
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    text: str = 'Выберите категорию устройства: \n '

    await bot.edit_message_text(text=text,
                                chat_id=chat_id,
                                message_id=message_id,
                                reply_markup=
                                get_device_category_keyboard(
                                    names_for_buttons=
                                    all_device_category))


@router_for_catalog.callback_query(ForDeleteMesage.filter())
async def get_device_category(message: types.Message):
    chat_id = message.message.chat.id
    message_id = message.message.message_id

    await bot.delete_message(chat_id=chat_id, message_id=message_id)


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


@router_for_catalog.callback_query(SelectNameDevices.filter())
@router_for_catalog.callback_query(SelectManufacturers.filter())
async def get_name_devices(callback: CallbackQuery,
                           callback_data: SelectManufacturers,
                           names_devices,
                           state: FSMContext):
    manufacturer = callback_data.manufacturer
    device_category = callback_data.device_category

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    if hasattr(callback_data, 'name_device'):

        name_device = callback_data.name_device
        data = await state.get_data()

        if len(data) == 0:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)

        if not name_device in data.values():
            await state.update_data({'name_selected_device': name_device})
            devices = await db.info_about_devices(name_device=name_device)

            inform_about_name_device: str = ''

            photo = FSInputFile(path='')

            for one_device in devices:
                inform_about_name_device += \
                    'Характеристики:\n' + one_device[4] + '\n' + \
                    'Цена: ' + str(one_device[5]) + '\n' + \
                    'Количество: ' + str(one_device[6]) + '\n\n'

                photo = FSInputFile(path=one_device[7])

            text: str = 'Выберите модель устройства: \n'

            await bot.send_photo(chat_id=chat_id,
                                 photo=photo,
                                 caption=inform_about_name_device + text,
                                 reply_markup=
                                 get_name_devices_keyboard(
                                     manufacturer=manufacturer,
                                     device_category=device_category,
                                     names_for_buttons=names_devices))
    else:
        text: str = 'Выберите модель устройства: \n'

        await bot.edit_message_text(text=text,
                                    chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=
                                    get_name_devices_keyboard(
                                        manufacturer=manufacturer,
                                        device_category=device_category,
                                        names_for_buttons=names_devices))
