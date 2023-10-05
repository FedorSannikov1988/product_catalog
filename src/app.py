from middlewares import GetDeviceCategoryStart, \
                        GetDeviceManufacturer, \
                        GetDeviceCategoryBack, \
                        GetDevicesNames, \
                        StartGalleryDevices, \
                        ActionRightLeftGalleryDevices, \
                        GetDevicesNamesAndDevice
from handlers import router_for_start_action, router_for_catalog
from loader import bot, dp
import asyncio


async def main():

    router_for_catalog.message.middleware(GetDeviceCategoryStart())
    router_for_catalog.callback_query.middleware(GetDeviceCategoryBack())
    router_for_catalog.callback_query.middleware(GetDeviceManufacturer())
    router_for_catalog.callback_query.middleware(GetDevicesNames())
    router_for_catalog.callback_query.middleware(StartGalleryDevices())
    router_for_catalog.callback_query.middleware(ActionRightLeftGalleryDevices())
    router_for_catalog.callback_query.middleware(GetDevicesNamesAndDevice())

    dp.include_router(router_for_start_action)
    dp.include_router(router_for_catalog)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
