from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from loader import router_for_catalog, bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram import types, F
from keyboards import get_name_information_picture_devices_keyboard, \
                      get_device_category_keyboard, \
                      get_manufacturers_keyboard, \
                      get_name_devices_keyboard, \
                      for_gallery_devices, \
                      SelectDeviceCategory, \
                      SelectManufacturers, \
                      SelectNameDevices, \
                      ForDeleteMesage, \
                      BackGetNameDevices, \
                      BackGetManufacturers, \
                      BackGetNameInformationPictureDevices, \
                      BackGetManufacturersFromGalleryDevices, \
                      GetGalleryDevices,  \
                      ActionGalleryDevices


@router_for_catalog.message(Command("catalog"))
async def get_device_category(message: types.Message,
                              all_device_category: list):
    text: str = 'Выберите категорию устройства: \n'

    args_for_answer = {
        'text': text,
        'reply_markup': get_device_category_keyboard(
            names_for_buttons=all_device_category)
    }
    await message.answer(**args_for_answer)


@router_for_catalog.callback_query(BackGetManufacturersFromGalleryDevices.filter())
@router_for_catalog.callback_query(BackGetManufacturers.filter())
async def back_get_device_category(callback: CallbackQuery,
                                   all_device_category: list):
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    text: str = 'Выберите категорию устройства: \n '

    search_callback_one: str = 'back_gallery_devices'

    if not search_callback_one in callback.data:
        args_for_edit_message_text = {
            'text': text,
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': get_device_category_keyboard(
                names_for_buttons=all_device_category)
        }
        await bot.edit_message_text(**args_for_edit_message_text)

    else:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

        args_for_send_message = {
            'text': text,
            'chat_id': chat_id,
            'reply_markup': get_device_category_keyboard(
                names_for_buttons=all_device_category)
        }
        await bot.send_message(**args_for_send_message)


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

    text_available_in_stock: str = 'Выберите производителя устройства: \n'
    text_out_of_stock: str = 'На данный момент устройств этой категории нет на складе'

    search_callback_one: str = 'back_get_devices_picture_information_name'

    if not search_callback_one in callback.data:

        if not manufacturers:
            await callback.answer(
                text=text_out_of_stock,
                show_alert=False
            )
        else:
            args_for_edit_message_text = {
                'text': text_available_in_stock,
                'chat_id': chat_id,
                'message_id': message_id,
                'reply_markup': get_manufacturers_keyboard(
                    device_category=device_category,
                    names_for_buttons=manufacturers)
            }
            await bot.edit_message_text(**args_for_edit_message_text)
    else:

        await bot.delete_message(chat_id=chat_id, message_id=message_id)

        args_for_send_message = {
            'text': text_available_in_stock,
            'chat_id': chat_id,
            'reply_markup': get_manufacturers_keyboard(
                device_category=device_category,
                names_for_buttons=manufacturers)
        }
        await bot.send_message(**args_for_send_message)


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

    args_for_edit_message_text = {
        'text': text,
        'chat_id': chat_id,
        'message_id': message_id,
        'reply_markup': get_name_devices_keyboard(
            manufacturer=manufacturer,
            device_category=device_category,
            names_for_buttons=names_devices)
    }
    await bot.edit_message_text(**args_for_edit_message_text)


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

    photo = FSInputFile(path=devices[0][7])

    inform_about_name_device: str = ''

    for one_device in devices:
        inform_about_name_device += \
            '\n' + one_device[4] + '\n' + \
            'Цена: ' + str(one_device[5]) + '\n' + \
            'Количество: ' + str(one_device[6]) + '\n\n'

    text: str = \
        f'Модель устройства: {hbold(names_devices[0])}\n\n' + 'Характеристики и цена:\n'

    args_for_send_photo = {
        'photo': photo,
        'caption': (text + inform_about_name_device),
        'chat_id': chat_id,
        'reply_markup': get_name_information_picture_devices_keyboard(
            manufacturer=manufacturer,
            device_category=device_category,
            names_for_buttons=names_devices)
    }
    await bot.send_photo(**args_for_send_photo)


@router_for_catalog.callback_query(GetGalleryDevices.filter())
async def get_gallery_devices(callback: CallbackQuery,
                              callback_data: GetGalleryDevices,
                              device_for_start_gallery: list,
                              number_pages: int,
                              state: FSMContext):

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    manufacturer = callback_data.manufacturer
    device_category = callback_data.device_category

    start_name_device: str = device_for_start_gallery[0][3]

    photo = FSInputFile(path=device_for_start_gallery[0][7])

    text: str = \
        f'Модель устройства: {hbold(start_name_device)}\n\n' + 'Характеристики и цена:\n'

    inform_about_name_device: str = ''

    for one_device in device_for_start_gallery:
        inform_about_name_device += \
            '\n' + one_device[4] + '\n' + \
            'Цена: ' + str(one_device[5]) + '\n' + \
            'Количество: ' + str(one_device[6]) + '\n\n'

    inform_about_name_device += \
        '{word_str:>40} {number_str}/{all_str}'.format(word_str='страниц',
                                                       number_str=1,
                                                       all_str=number_pages)

    data_from_previous_message = await state.get_data()
    search_data_from_previous_message: str = 'needs be deleted this message'

    if not search_data_from_previous_message in data_from_previous_message.values():

        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     (text + inform_about_name_device)),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(manufacturer=
                                                manufacturer,
                                                device_category=
                                                device_category,
                                                selected_devices=
                                                start_name_device)
        }
        await bot.edit_message_media(**args_for_edit_message_media)

    else:
        await state.clear()
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

        args_for_send_photo = {
            'photo': photo,
            'caption': (text + inform_about_name_device),
            'chat_id': chat_id,
            'reply_markup': for_gallery_devices(manufacturer=
                                                manufacturer,
                                                selected_devices=
                                                start_name_device,
                                                device_category=
                                                device_category)
        }
        await bot.send_photo(**args_for_send_photo)


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.turn == "right"))
async def action_right_gallery_devices(callback: CallbackQuery,
                                       callback_data: ActionGalleryDevices,
                                       devices_for_action: list):

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    manufacturer = callback_data.manufacturer
    device_category = callback_data.device_category
    see_name_device = callback_data.see_name_device

    names_devices = list()

    for one_device in devices_for_action:
        names_devices.append(one_device[3])

    names_devices = list(set(names_devices))

    names_devices.sort()

    size_names_devices = len(names_devices)
    index_see_name_device = names_devices.index(see_name_device)
    index_new_name_device = index_see_name_device + 1

    if (size_names_devices > 1) and \
       (size_names_devices > index_new_name_device):

        new_name_device = names_devices[index_new_name_device]

        choose_device = list()

        for one_device in devices_for_action:
            if one_device[3] == new_name_device:
                choose_device.append(one_device)

        photo = FSInputFile(path=choose_device[0][7])

        text: str = \
            f'Модель устройства: {hbold(new_name_device)}\n\n' + 'Характеристики и цена:\n'

        inform_about_name_device: str = ''

        for one_device in choose_device:
            inform_about_name_device += \
                '\n' + one_device[4] + '\n' + \
                'Цена: ' + str(one_device[5]) + '\n' + \
                'Количество: ' + str(one_device[6]) + '\n\n'

        inform_about_name_device += \
            '{word_str:>40} {number_str}/{all_str}'.format(word_str='страница',
                                                           number_str=index_new_name_device+1,
                                                           all_str=size_names_devices)

        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     (text + inform_about_name_device)),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(selected_devices=new_name_device,
                                                manufacturer=manufacturer,
                                                device_category=device_category)
        }
        await bot.edit_message_media(**args_for_edit_message_media)


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.turn == "left"))
async def action_left_gallery_devices(callback: CallbackQuery,
                                      callback_data: ActionGalleryDevices,
                                      devices_for_action: list):

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    manufacturer = callback_data.manufacturer
    device_category = callback_data.device_category
    see_name_device = callback_data.see_name_device

    names_devices = list()

    for one_device in devices_for_action:
        names_devices.append(one_device[3])

    names_devices = list(set(names_devices))

    names_devices.sort()

    size_names_devices = len(names_devices)
    index_see_name_device = names_devices.index(see_name_device)
    index_new_name_device = index_see_name_device - 1

    if (size_names_devices > 1) and \
       (index_new_name_device >= 0):

        new_name_device = names_devices[index_new_name_device]

        choose_device = list()

        for one_device in devices_for_action:
            if one_device[3] == new_name_device:
                choose_device.append(one_device)

        photo = FSInputFile(path=choose_device[0][7])

        text: str = \
            f'Модель устройства: {hbold(new_name_device)}\n\n' + 'Характеристики и цена:\n'

        inform_about_name_device: str = ''

        for one_device in choose_device:
            inform_about_name_device += \
                '\n' + one_device[4] + '\n' + \
                'Цена: ' + str(one_device[5]) + '\n' + \
                'Количество: ' + str(one_device[6]) + '\n\n'

        inform_about_name_device += \
            '{word_str:>40} {number_str}/{all_str}'.format(word_str='страница',
                                                           number_str=index_new_name_device+1,
                                                           all_str=size_names_devices)

        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     (text + inform_about_name_device)),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(selected_devices=new_name_device,
                                                manufacturer=manufacturer,
                                                device_category=device_category)
        }
        await bot.edit_message_media(**args_for_edit_message_media)


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.pin_message == 'pin it'))
async def pin_gallery_devices(callback: CallbackQuery,
                              callback_data: ActionGalleryDevices,
                              devices_for_action):
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    manufacturer = callback_data.manufacturer
    device_category = callback_data.device_category
    see_name_device = callback_data.see_name_device

    names_devices = list()

    for one_device in devices_for_action:
        names_devices.append(one_device[3])

    names_devices = list(set(names_devices))

    names_devices.sort()

    size_names_devices = len(names_devices)
    index_see_name_device = names_devices.index(see_name_device)

    choose_device = list()

    for one_device in devices_for_action:
        if one_device[3] == see_name_device:
            choose_device.append(one_device)

    photo = FSInputFile(path=choose_device[0][7])

    text: str = \
        f'Модель устройства: {hbold(see_name_device)}\n\n' + 'Характеристики и цена:\n'

    inform_about_name_device: str = ''

    for one_device in choose_device:
        inform_about_name_device += \
            '\n' + \
            'Характеристики:\n' + one_device[4] + '\n' + \
            'Цена: ' + str(one_device[5]) + '\n' + \
            'Количество: ' + str(one_device[6]) + '\n\n'

    inform_about_name_device += \
        '{word_str:>40} {number_str}/{all_str}'.format(word_str='страница',
                                                       number_str=index_see_name_device + 1,
                                                       all_str=size_names_devices)

    message_id_for_pin = await bot.copy_message(chat_id=chat_id, message_id=message_id, from_chat_id=chat_id)

    await bot.delete_message(chat_id=chat_id, message_id=message_id)

    await bot.pin_chat_message(chat_id=chat_id, message_id=message_id_for_pin.message_id)

    args_for_send_photo = {
        'photo': photo,
        'caption': (text + inform_about_name_device),
        'chat_id': chat_id,
        'reply_markup': for_gallery_devices(manufacturer=
                                            manufacturer,
                                            selected_devices=
                                            see_name_device,
                                            device_category=
                                            device_category)
    }
    await bot.send_photo(**args_for_send_photo)
