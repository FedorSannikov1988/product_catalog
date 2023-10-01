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
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:

        search_callback_one: str = 'device_category:'
        search_callback_two: str = 'back_get_devices_name:'
        search_callback_three: str = 'back_get_devices_picture_information_name:'

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


class GetDevicesNamesAndDevices(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:

        search_callback_one: str = 'manufacturers:'
        search_callback_two: str = 'name_devices:'

        if (search_callback_one in event.data) or \
           (search_callback_two in event.data):

            category_and_manufacturer = event.data.split(':')
            manufacturer = category_and_manufacturer[2]
            category = category_and_manufacturer[1]

            # для get_name_information_picture_devices
            if (search_callback_two in event.data) and \
               len(category_and_manufacturer) == 4:

                name_device = category_and_manufacturer[3]
                data['devices'] = await db.info_about_devices(name_device=
                                                              name_device)

            devices_from_db = \
                await db.info_about_devices(name_category=category,
                                            name_manufacturer=manufacturer)
            if devices_from_db:

                names_devices: list = []

                for one_device in devices_from_db:
                    names_devices.append(one_device[3])

                data['names_devices'] = list(set(names_devices))

            else:
                data['names_devices'] = list()

        #if search_callback_two in event.data:
        #    for_name_device = event.data.split(':')
        #    name_device = for_name_device[3]
        #    data['devices'] = await db.info_about_devices(name_device=name_device)

        return await handler(event, data)


class GetDevices(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:

        search_callback_one: str = 'gallery_devices:'

        if search_callback_one in event.data:
            prefix_and_names_devices = event.data.split(':')
            names_devices = prefix_and_names_devices[1].split(';')

        return await handler(event, data)