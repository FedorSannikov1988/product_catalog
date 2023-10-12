"""
Loading data from database for handlers.
"""
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import Message, CallbackQuery
from aiogram import BaseMiddleware
from loader import db


class GetDeviceCategoryStart(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        """
        To download all product categories from the database
        for handler: get_device_category.

        :param handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]]
        :param event: Message
        :param data: Dict[str, Any]
        :return: Awaitable
        """
        search_text_one: str = '/catalog'

        if search_text_one == event.text:

            all_device_category: list = []

            all_device_category_from_db = await db.info_all_device_category()

            for one_category in all_device_category_from_db:
                all_device_category.append(one_category[1])

            data['all_device_category'] = all_device_category

        return await handler(event, data)


class GetDeviceCategoryBack(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        """
        To download all product categories from the database
        for handler: back_get_device_category.
        Back from category device and gallery devices.

        :param handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]]
        :param event: Message
        :param data: Dict[str, Any]
        :return: Awaitable
        """
        search_callback_one: str = 'back_get_category_device'
        search_callback_two: str = 'back_gallery_devices'

        if (search_callback_one in event.data) or (search_callback_two in event.data):

            all_device_category: list = []

            all_device_category_from_db = await db.info_all_device_category()

            for one_category in all_device_category_from_db:
                all_device_category.append(one_category[1])

            data['all_device_category'] = all_device_category

        return await handler(event, data)


class GetDeviceManufacturer(BaseMiddleware):
    """
    To download manufacturers from database for select product category
    for handler:back_get_device_category, get_manufacturers, get_name_devices

    :param handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]]
    :param event: Message
    :param data: Dict[str, Any]
    :return: Awaitable
    """
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:

        search_callback_one: str = 'device_category:'
        search_callback_two: str = 'back_name_devices:'
        search_callback_three: str = 'back_devices_name_and_picture:'

        if (search_callback_one in event.data) or \
           (search_callback_two in event.data) or \
           (search_callback_three in event.data):

            device_category = event.data.split(':')
            device_category = device_category[1]

            devices_right_category_from_db = \
                await db.info_about_devices(name_category=
                                            device_category)

            if devices_right_category_from_db:

                all_manufacturers: list = []

                for one_device_right_category in devices_right_category_from_db:
                    all_manufacturers.append(one_device_right_category[1])

                data['manufacturers'] = list(set(all_manufacturers))
            else:
                data['manufacturers'] = list()

        return await handler(event, data)


class GetDevicesNames(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        """
        To download device models from the database for handlers:
        get_name_devices .

        :param handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]]
        :param event: Message
        :param data: Dict[str, Any]
        :return: Awaitable
        """

        search_callback_one: str = 'manufacturers:'

        if search_callback_one in event.data:

            fsm_state: dict = await data['state'].get_data()

            prefix_and_manufacturer = event.data.split(':')
            manufacturer = prefix_and_manufacturer[1]
            category = fsm_state['device_category']

            devices_from_db = \
                await db.info_about_devices(name_category=category,
                                            name_manufacturer=manufacturer)

            names_devices: list = []

            for one_device in devices_from_db:
                names_devices.append(one_device[3])

            data['names_devices'] = list(set(names_devices))

        return await handler(event, data)


class GetDevicesNamesAndDevice(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        """
        To download device models (names_devices) and devices
        (previously selected: device_category, manufacturer')
        from the database for handlers:
        get_name_information_picture_devices .

        :param handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]]
        :param event: Message
        :param data: Dict[str, Any]
        :return: Awaitable
        """

        search_callback_one: str = 'name_device:'

        if search_callback_one in event.data:

            prefix_and_name_device = event.data.split(':')
            name_device = prefix_and_name_device[1]

            fsm_state: dict = await data['state'].get_data()
            category = fsm_state['device_category']
            manufacturer = fsm_state['manufacturer']

            devices_from_db = \
                await db.info_about_devices(name_category=category,
                                            name_manufacturer=manufacturer)

            devices: list = []
            names_devices: list = []

            for one_device in devices_from_db:
                names_devices.append(one_device[3])
                if name_device == one_device[3]:
                    devices.append(one_device)

            data['names_devices'] = list(set(names_devices))
            data['devices'] = devices

        return await handler(event, data)


class StartGalleryDevices(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        """
        To download from the database (with pretreatment) variable
        device_for_start_gallery and number_pages = len(names_devices)
        for handlers: get_gallery_devices .

        :param handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]]
        :param event: Message
        :param data: Dict[str, Any]
        :return: Awaitable
        """

        search_callback_one: str = 'start_gallery_devices'

        if search_callback_one in event.data:
            fsm_state: dict = await data['state'].get_data()
            category = fsm_state['device_category']
            manufacturer = fsm_state['manufacturer']

            devices = \
                await db.info_about_devices(name_category=category,
                                            name_manufacturer=manufacturer)

            names_devices = list()

            for one_device in devices:
                names_devices.append(one_device[3])

            names_devices = list(set(names_devices))

            names_devices.sort()

            device_for_start_gallery = list()

            for one_device in devices:
                if names_devices[0] == one_device[3]:
                    device_for_start_gallery.append(one_device)

            data['number_pages'] = len(names_devices)
            data['device_for_start_gallery'] = device_for_start_gallery

        return await handler(event, data)


class ActionRightLeftGalleryDevices(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        """
        To download from the database devices (variable devices_for_action)
        selected device_category and manufacturer for handlers:
        action_right_gallery_devices, action_left_gallery_devices,
        pin_gallery_devices.

        :param handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]]
        :param event: Message
        :param data: Dict[str, Any]
        :return: Awaitable
        """

        search_callback_one: str = 'action_gallery_devices:'

        if search_callback_one in event.data:
            fsm_state: dict = await data['state'].get_data()
            category = fsm_state['device_category']
            manufacturer = fsm_state['manufacturer']

            devices_for_action = await db.info_about_devices(name_category=category,
                                                             name_manufacturer=manufacturer)
            data['devices_for_action'] = devices_for_action

        return await handler(event, data)
