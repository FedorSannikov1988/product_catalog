"""
Responsible for displaying the product catalog.
"""
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
                      ForDeleteMessage, \
                      BackGetNameDevices, \
                      BackGetManufacturers, \
                      BackGetNameInformationPictureDevices, \
                      BackGetManufacturersFromGalleryDevices, \
                      GetGalleryDevices,  \
                      ActionGalleryDevices


@router_for_catalog.message(Command("catalog"))
async def get_device_category(message: types.Message,
                              all_device_category: list):
    """
    Launching the product catalog .

    :param message: types.Message
    :param all_device_category: list
    :return: None
    """
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
    """
    Return to the device category selection .

    :param callback: CallbackQuery
    :param all_device_category: list
    :return: None
    """
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


@router_for_catalog.callback_query(ForDeleteMessage.filter())
async def delete_mesage(message: types.Message, state: FSMContext):
    """
    To delete messages and reset the state variable
    (stores FSMContext) when the "Finish" button
    is clicked.

    :param message: types.Message
    :param state: FSMContext
    :return: None
    """
    chat_id = message.message.chat.id
    message_id = message.message.message_id

    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await state.clear()


@router_for_catalog.callback_query(BackGetNameInformationPictureDevices.filter())
@router_for_catalog.callback_query(BackGetNameDevices.filter())
@router_for_catalog.callback_query(SelectDeviceCategory.filter())
async def get_manufacturers(callback: CallbackQuery,
                            callback_data: SelectDeviceCategory,
                            state: FSMContext,
                            manufacturers: list):
    """
    To select the device manufacturer.

    :param callback: CallbackQuery
    :param callback_data: SelectDeviceCategory
    :param state: FSMContext
    :param manufacturers: list
    :return: None
    """
    manufacturers.sort()

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    device_category = callback_data.device_category

    await state.update_data({'device_category': device_category})

    text_available_in_stock: str = \
        f"{hbold(device_category)} \n" + 'Выберите производителя устройства: \n'

    text_out_of_stock: str = \
        'На данный момент устройств этой категории нет на складе'

    search_callback_one: str = 'back_devices_name_and_picture'

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
                    names_for_buttons=manufacturers)
            }
            await bot.edit_message_text(**args_for_edit_message_text)
    else:

        await bot.delete_message(chat_id=chat_id, message_id=message_id)

        args_for_send_message = {
            'text': text_available_in_stock,
            'chat_id': chat_id,
            'reply_markup': get_manufacturers_keyboard(
                names_for_buttons=manufacturers)
        }
        await bot.send_message(**args_for_send_message)


@router_for_catalog.callback_query(SelectManufacturers.filter())
async def get_name_devices(callback: CallbackQuery,
                           callback_data: SelectManufacturers,
                           names_devices: list,
                           state: FSMContext):
    """
    Selection of the device by name (the choice of
    category and manufacturer was made earlier).

    :param callback: CallbackQuery
    :param callback_data: SelectManufacturers
    :param names_devices: list
    :param state: FSMContext
    :return: None
    """
    names_devices.sort()

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    manufacturer = callback_data.manufacturer

    await state.update_data({'manufacturer': manufacturer,
                             'mark_for_delete': 'needs be deleted this message'})
    for_device_category: dict = await state.get_data()

    text: str = \
        f"{hbold(for_device_category['device_category'])} → " \
        f"{hbold(manufacturer)} \n" + \
        "Выберите модель устройства: \n"

    args_for_edit_message_text = {
        'text': text,
        'chat_id': chat_id,
        'message_id': message_id,
        'reply_markup': get_name_devices_keyboard(
            device_category=for_device_category['device_category'],
            names_for_buttons=names_devices)
    }
    await bot.edit_message_text(**args_for_edit_message_text)


@router_for_catalog.callback_query(SelectNameDevices.filter())
async def get_name_information_picture_devices(callback: CallbackQuery,
                                               names_devices: list,
                                               devices: list,
                                               state: FSMContext):
    """
    Displays information about the selected
    model and a picture of the device .

    :param callback: CallbackQuery
    :param names_devices: list
    :param devices: list
    :param state: FSMContext
    :return: None
    """
    names_devices.sort()

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    for_delete_message_and_device_category: dict = await state.get_data()
    value_where_looking = for_delete_message_and_device_category.get('mark_for_delete')
    search_for_delete_message: str = 'needs be deleted this message'

    if value_where_looking is not None and \
            search_for_delete_message in value_where_looking:

        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        await state.update_data({'mark_for_delete': ''})

    photo = FSInputFile(path=devices[0][7])

    inform_about_name_device: str = for_print_inform(devices=devices)

    text: str = \
        f'Модель устройства: {hbold(devices[0][3])}\n\n' + 'Характеристики и цена:\n'

    args_for_send_photo = {
        'photo': photo,
        'caption': (text + inform_about_name_device),
        'chat_id': chat_id,
        'reply_markup': get_name_information_picture_devices_keyboard(
            device_category=for_delete_message_and_device_category['device_category'],
            names_for_buttons=names_devices)
    }
    await bot.send_photo(**args_for_send_photo)


@router_for_catalog.callback_query(GetGalleryDevices.filter())
async def get_gallery_devices(callback: CallbackQuery,
                              device_for_start_gallery: list,
                              number_pages: int,
                              state: FSMContext):
    """
    Output of the gallery of products (picture and information
    about the product of the selected category and manufacturer)
    with the ability to scroll.

    :param callback: CallbackQuery
    :param device_for_start_gallery: list
    :param number_pages: int
    :param state: FSMContext
    :return: None
    """
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    index_selected_devices: int = 0
    start_name_device: str = device_for_start_gallery[index_selected_devices][3]
    photo = FSInputFile(path=device_for_start_gallery[index_selected_devices][7])

    text: str = \
        f'Модель устройства: {hbold(start_name_device)}\n\n' + 'Характеристики и цена:\n'

    inform_about_name_device: str = for_print_inform(devices=device_for_start_gallery)

    inform_about_name_device += for_page_numbering(all_str=number_pages,
                                                   number_str=1)

    for_delete_message: dict = await state.get_data()
    value_where_looking = for_delete_message.get('mark_for_delete')
    search_for_delete_message: str = 'needs be deleted this message'

    if value_where_looking is not None \
            and not search_for_delete_message in value_where_looking:

        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     (text + inform_about_name_device)),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(index_selected_devices=
                                                index_selected_devices)
        }
        await bot.edit_message_media(**args_for_edit_message_media)

    else:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        await state.update_data({'mark_for_delete': ''})

        args_for_send_photo = {
            'photo': photo,
            'caption': (text + inform_about_name_device),
            'chat_id': chat_id,
            'reply_markup': for_gallery_devices(index_selected_devices=
                                                index_selected_devices)
        }
        await bot.send_photo(**args_for_send_photo)


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.turn == "right"))
async def action_right_gallery_devices(callback: CallbackQuery,
                                       callback_data: ActionGalleryDevices,
                                       devices_for_action: list):
    """
    Scroll the product gallery to the right (if the number of sheets allows).

    :param callback: CallbackQuery
    :param callback_data: ActionGalleryDevices
    :param devices_for_action: list
    :return: None
    """
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    index_see_name_device = callback_data.index_see_name_device

    names_devices = list()

    for one_device in devices_for_action:
        names_devices.append(one_device[3])

    names_devices = list(set(names_devices))

    names_devices.sort()

    size_names_devices = len(names_devices)
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

        inform_about_name_device: str = for_print_inform(devices=choose_device)

        inform_about_name_device += for_page_numbering(all_str=size_names_devices,
                                                       number_str=index_new_name_device + 1)

        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     (text + inform_about_name_device)),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(index_selected_devices=
                                                index_new_name_device)
        }
        await bot.edit_message_media(**args_for_edit_message_media)


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.turn == "left"))
async def action_left_gallery_devices(callback: CallbackQuery,
                                      callback_data: ActionGalleryDevices,
                                      devices_for_action: list):
    """
    Scroll the product gallery to the left (if the number of sheets allows).

    :param callback: CallbackQuery
    :param callback_data: ActionGalleryDevices
    :param devices_for_action: list
    :return: None
    """
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    index_see_name_device = callback_data.index_see_name_device

    names_devices = list()

    for one_device in devices_for_action:
        names_devices.append(one_device[3])

    names_devices = list(set(names_devices))

    names_devices.sort()

    size_names_devices = len(names_devices)
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

        inform_about_name_device: str = for_print_inform(devices=choose_device)

        inform_about_name_device += for_page_numbering(all_str=size_names_devices,
                                                       number_str=index_new_name_device+1)

        args_for_edit_message_media = {
            'media': InputMediaPhoto(media=photo,
                                     caption=
                                     (text + inform_about_name_device)),
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': for_gallery_devices(index_selected_devices=
                                                index_new_name_device)
        }
        await bot.edit_message_media(**args_for_edit_message_media)


@router_for_catalog.callback_query(ActionGalleryDevices.filter(F.pin_message == 'pin it'))
async def pin_gallery_devices(callback: CallbackQuery,
                              callback_data: ActionGalleryDevices,
                              devices_for_action: list):
    """
    Fixing the product you like.

    :param callback: CallbackQuery
    :param callback_data: ActionGalleryDevices
    :param devices_for_action: list
    :return: None
    """
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    index_see_name_device = callback_data.index_see_name_device

    names_devices = list()

    for one_device in devices_for_action:
        names_devices.append(one_device[3])

    names_devices = list(set(names_devices))

    names_devices.sort()

    size_names_devices = len(names_devices)
    see_name_device = names_devices[index_see_name_device]

    choose_device = list()

    for one_device in devices_for_action:
        if one_device[3] == see_name_device:
            choose_device.append(one_device)

    photo = FSInputFile(path=choose_device[0][7])

    text: str = \
        f'Модель устройства: {hbold(see_name_device)}\n\n' + 'Характеристики и цена:\n'

    inform_about_name_device: str = for_print_inform(devices=choose_device)

    inform_about_name_device += for_page_numbering(all_str=size_names_devices,
                                                   number_str=index_see_name_device + 1)

    message_id_for_pin = await bot.copy_message(chat_id=chat_id, message_id=message_id, from_chat_id=chat_id)

    await bot.delete_message(chat_id=chat_id, message_id=message_id)

    await bot.pin_chat_message(chat_id=chat_id, message_id=message_id_for_pin.message_id)

    args_for_send_photo = {
        'photo': photo,
        'caption': (text + inform_about_name_device),
        'chat_id': chat_id,
        'reply_markup': for_gallery_devices(index_selected_devices=
                                            index_see_name_device)
    }
    await bot.send_photo(**args_for_send_photo)


def for_print_inform(devices: list):
    """
    To generate output information about the product.

    :param devices: list
    :return: str
    """
    inform_about_name_device: str = ''

    for one_device in devices:
        inform_about_name_device += \
            '\n' + \
            'Характеристики:\n' + one_device[4] + '\n' + \
            f'{hbold("Цена:")} ' + str(int(one_device[5])) + ' ₽\n' + \
            f'{hbold("Количество:")} ' + str(one_device[6]) + ' штук \n'

    return inform_about_name_device


def for_page_numbering(all_str: int,
                       number_str: int):
    """
    To display the page number in the product galleries.

    :param all_str: int
    :param number_str: int
    :return: str
    """

    page_numbering = \
        '{word_str:>40} {number_str}/{all_str}'.format(word_str='страница',
                                                       number_str=number_str,
                                                       all_str=all_str)

    return page_numbering
