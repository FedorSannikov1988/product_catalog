from keyboards import BackGetNameDevices, \
    get_name_information_picture_devices_keyboard, \
    get_device_category_keyboard, \
    get_manufacturers_keyboard, \
    get_name_devices_keyboard, \
    SelectDeviceCategory, \
    SelectManufacturers, \
    SelectNameDevices, \
    ForDeleteMesage, \
    BackGetManufacturers, BackGetNameInformationPictureDevices, GetGalleryDevices, for_gallery_devices, \
    BackGetManufacturersFromGalleryDevices, ActionGalleryDevices
from middlewares import GetDeviceCategoryStart, \
    GetDeviceManufacturer, \
    GetDeviceCategoryBack, \
    GetDevicesNamesAndDevices
from loader import router_for_catalog, bot, db
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, \
    FSInputFile, InputMediaPhoto
from aiogram.filters import Command
from aiogram import types
from aiogram import F

router_for_catalog.message.middleware(GetDeviceCategoryStart())
router_for_catalog.callback_query.middleware(GetDeviceCategoryBack())
router_for_catalog.callback_query.middleware(GetDeviceManufacturer())
router_for_catalog.callback_query.middleware(GetDevicesNamesAndDevices())


@router_for_catalog.message(Command("catalog"))
async def get_device_category(message: types.Message,
                              all_device_category: list):
    text: str = 'Выберите категорию устройства: \n '

    await message.answer(text=text,
                         reply_markup=
                         get_device_category_keyboard(
                             names_for_buttons=
                             all_device_category))


@router_for_catalog.callback_query(BackGetManufacturersFromGalleryDevices.filter())
@router_for_catalog.callback_query(BackGetManufacturers.filter())
async def back_get_device_category(callback: CallbackQuery,
                                   all_device_category: list):
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    search_callback_one: str = 'back_gallery_devices'
    text: str = 'Выберите категорию устройства: \n '

    if not search_callback_one in callback.data:
        await bot.edit_message_text(text=text,
                                    chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=
                                    get_device_category_keyboard(
                                        names_for_buttons=
                                        all_device_category))
    else:
        await bot.delete_message(chat_id=chat_id,
                                 message_id=message_id)

        await bot.send_message(text=text,
                               chat_id=chat_id,
                               reply_markup=
                               get_device_category_keyboard(
                                   names_for_buttons=
                                   all_device_category))


@router_for_catalog.callback_query(ForDeleteMesage.filter())
async def delete_mesage(message: types.Message):
    chat_id = message.message.chat.id
    message_id = message.message.message_id

    await bot.delete_message(chat_id=chat_id, message_id=message_id)


@router_for_catalog.callback_query(BackGetNameInformationPictureDevices.filter())
@router_for_catalog.callback_query(BackGetNameDevices.filter())
@router_for_catalog.callback_query(SelectDeviceCategory.filter())
async def get_manufacturers(callback: CallbackQuery,
                            callback_data: SelectDeviceCategory,
                            manufacturers: list):
    manufacturers.sort()

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    device_category = callback_data.device_category

    text: str = 'Выберите производителя устройства: \n'

    search_callback_one: str = 'back_get_devices_picture_information_name'

    if not search_callback_one in callback.data:

        if not manufacturers:
            await callback.answer(
                text="На данный момент устройств этой категории нет на складе",
                show_alert=False
            )
        else:

            await bot.edit_message_text(text=text,
                                        chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=
                                        get_manufacturers_keyboard(
                                            device_category=
                                            device_category,
                                            names_for_buttons=
                                            manufacturers))
    else:
        await bot.delete_message(chat_id=chat_id,
                                 message_id=message_id)

        await bot.send_message(text=text,
                               chat_id=chat_id,
                               reply_markup=
                               get_manufacturers_keyboard(
                                   device_category=
                                   device_category,
                                   names_for_buttons=
                                   manufacturers))


@router_for_catalog.callback_query(SelectManufacturers.filter())
async def get_name_devices(callback: CallbackQuery,
                           callback_data: SelectManufacturers,
                           names_devices: list,
                           state: FSMContext):
    await state.update_data({'fer_delete': 'needs be deleted this message'})

    names_devices.sort()

    manufacturer = callback_data.manufacturer
    device_category = callback_data.device_category

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    text: str = 'Выберите модель устройства: \n'

    await bot.edit_message_text(text=text,
                                chat_id=chat_id,
                                message_id=message_id,
                                reply_markup=
                                get_name_devices_keyboard(
                                    manufacturer=manufacturer,
                                    device_category=device_category,
                                    names_for_buttons=names_devices))


@router_for_catalog.callback_query(SelectNameDevices.filter())
async def get_name_information_picture_devices(callback: CallbackQuery,
                                               callback_data: SelectNameDevices,
                                               names_devices, devices,
                                               state: FSMContext):
    manufacturer = callback_data.manufacturer
    device_category = callback_data.device_category

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    data_from_previous_message = await state.get_data()
    search_data_from_previous_message: str = 'needs be deleted this message'

    if search_data_from_previous_message in data_from_previous_message.values():
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        await state.clear()

    photo = FSInputFile(path='')
    inform_about_name_device: str = ''

    for one_device in devices:
        inform_about_name_device += \
            '\n' + \
            'Характеристики:\n' + one_device[4] + '\n' + \
            'Цена: ' + str(one_device[5]) + '\n' + \
            'Количество: ' + str(one_device[6]) + '\n\n'
        photo = FSInputFile(path=one_device[7])

    text: str = 'Выберите модель устройства: \n'

    await bot.send_photo(chat_id=chat_id,
                         photo=photo,
                         caption=inform_about_name_device + text,
                         reply_markup=
                         get_name_information_picture_devices_keyboard(
                             manufacturer=manufacturer,
                             device_category=device_category,
                             names_for_buttons=names_devices))


@router_for_catalog.callback_query(GetGalleryDevices.filter())
async def get_gallery_devices(callback: CallbackQuery,
                              callback_data: GetGalleryDevices,
                              state: FSMContext):

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    names_devices = callback_data.names_devices.split(';')

    devices = await db.info_about_devices(name_device=
                                          names_devices[0])

    text: str = 'Характеристики и цена: \n'

    photo = FSInputFile(path='')
    inform_about_name_device: str = ''

    for one_device in devices:
        inform_about_name_device += \
            '\n' + \
            'Характеристики:\n' + one_device[4] + '\n' + \
            'Цена: ' + str(one_device[5]) + '\n' + \
            'Количество: ' + str(one_device[6]) + '\n\n'
        photo = FSInputFile(path=one_device[7])

    inform_about_name_device += \
        '{word_str:>35} {number_str}/{all_str} '.format(word_str='страница',
                                                        number_str=1,
                                                        all_str=len(names_devices))

    data_from_previous_message = await state.get_data()
    search_data_from_previous_message: str = 'needs be deleted this message'

    if not search_data_from_previous_message in data_from_previous_message.values():
        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     text + inform_about_name_device),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(selected_devices=names_devices[0],
                                                all_names_devices=names_devices)
        }
        await bot.edit_message_media(**args_for_edit_message_media)

    else:
        await state.clear()
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        await bot.send_photo(chat_id=chat_id,
                             photo=photo,
                             caption=
                             text + inform_about_name_device,
                             reply_markup=for_gallery_devices(selected_devices=names_devices[0],
                                                              all_names_devices=names_devices))


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.turn == "left"))
async def get_gallery_devices(callback: CallbackQuery,
                              callback_data: ActionGalleryDevices):

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    see_name_device = callback_data.see_name_device
    names_devices = callback_data.all_names_devices.split(';')

    size_names_devices = len(names_devices)
    index_see_name_device = names_devices.index(see_name_device)
    index_new_name_device = index_see_name_device - 1

    if (size_names_devices > 1) and \
       (index_new_name_device >= 0):

        new_name_device = names_devices[index_new_name_device]
        devices = await db.info_about_devices(name_device=new_name_device)

        text: str = 'Характеристики и цена: \n'

        photo = FSInputFile(path='')
        inform_about_name_device: str = ''

        for one_device in devices:
            inform_about_name_device += \
                '\n' + \
                'Характеристики:\n' + one_device[4] + '\n' + \
                'Цена: ' + str(one_device[5]) + '\n' + \
                'Количество: ' + str(one_device[6]) + '\n\n'
            photo = FSInputFile(path=one_device[7])

        inform_about_name_device += \
            '{word_str:>35} {number_str}/{all_str} '.format(word_str='страница',
                                                            number_str=index_new_name_device+1,
                                                            all_str=len(names_devices))

        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     text + inform_about_name_device),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(selected_devices=new_name_device,
                                                all_names_devices=names_devices)
        }
        await bot.edit_message_media(**args_for_edit_message_media)


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.turn == "right"))
async def get_gallery_devices(callback: CallbackQuery,
                              callback_data: ActionGalleryDevices):

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    see_name_device = callback_data.see_name_device
    names_devices = callback_data.all_names_devices.split(';')

    size_names_devices = len(names_devices)
    index_see_name_device = names_devices.index(see_name_device)
    index_new_name_device = index_see_name_device + 1

    if (size_names_devices > 1) and \
       (size_names_devices > index_new_name_device):

        new_name_device = names_devices[index_new_name_device]
        devices = await db.info_about_devices(name_device=new_name_device)

        text: str = 'Характеристики и цена: \n'

        photo = FSInputFile(path='')
        inform_about_name_device: str = ''

        for one_device in devices:
            inform_about_name_device += \
                '\n' + \
                'Характеристики:\n' + one_device[4] + '\n' + \
                'Цена: ' + str(one_device[5]) + '\n' + \
                'Количество: ' + str(one_device[6]) + '\n\n'
            photo = FSInputFile(path=one_device[7])

        inform_about_name_device += \
            '{word_str:>35} {number_str}/{all_str} '.format(word_str='страница',
                                                            number_str=index_new_name_device+1,
                                                            all_str=len(names_devices))

        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     text + inform_about_name_device),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(selected_devices=new_name_device,
                                                all_names_devices=names_devices)
        }
        await bot.edit_message_media(**args_for_edit_message_media)


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.pin_message == 'pin it'))
async def get_gallery_devices(callback: CallbackQuery,
                              callback_data: ActionGalleryDevices):
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    see_name_device = callback_data.see_name_device
    names_devices = callback_data.all_names_devices.split(';')

    size_names_devices = len(names_devices)
    index_see_name_device = names_devices.index(see_name_device)
    index_new_name_device = index_see_name_device + 1

    devices = await db.info_about_devices(name_device=see_name_device)

    text: str = 'Характеристики и цена: \n'

    photo = FSInputFile(path='')
    inform_about_name_device: str = ''

    for one_device in devices:
        inform_about_name_device += \
            '\n' + \
            'Характеристики:\n' + one_device[4] + '\n' + \
            'Цена: ' + str(one_device[5]) + '\n' + \
            'Количество: ' + str(one_device[6]) + '\n\n'
        photo = FSInputFile(path=one_device[7])

    inform_about_name_device += \
        '{word_str:>35} {number_str}/{all_str} '.format(word_str='страница',
                                                        number_str=index_new_name_device,
                                                        all_str=size_names_devices)

    await bot.copy_message(chat_id=chat_id, message_id=message_id, from_chat_id=chat_id)

    await bot.pin_chat_message(chat_id=chat_id, message_id=message_id)

    await bot.send_photo(chat_id=chat_id,
                         photo=photo,
                         caption=
                         text + inform_about_name_device,
                         reply_markup=
                         for_gallery_devices(
                             selected_devices=names_devices[0],
                             all_names_devices=names_devices))

