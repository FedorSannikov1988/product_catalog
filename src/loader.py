from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Dispatcher, \
                    Bot
from db_api import Database_async
from loguru import logger
from config import TOKEN_BOT
from pathlib import Path
import aiosqlite
import asyncio

bot = Bot(token=TOKEN_BOT, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db_path = \
    Path('db_api', 'database', 'shop_database.db')
db = Database_async(db_path=db_path)

logger.add('logs/logs.json',
           level='DEBUG',
           format='{time} {level} {message}',
           rotation='10 MB',
           compression='zip',
           serialize=True)

try:
    loop = asyncio.get_event_loop()
    create_needs_tables = \
        [db.create_table_users(),
         db.create_table_products(),
         db.create_table_wallet_user(),
         db.create_table_shopping_cart()]
    loop.run_until_complete(asyncio.gather(*create_needs_tables))
except aiosqlite.OperationalError as sql_error:
    logger.error(sql_error)
except Exception as all_error:
    logger.error(all_error)
