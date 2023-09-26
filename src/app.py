from handlers import router_for_start_action, router_for_catalog
from loader import bot, dp
import asyncio


async def main():
    dp.include_router(router_for_start_action)
    dp.include_router(router_for_catalog)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
