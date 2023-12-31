"""
To download all the necessary data to
start the application /telegram bot
"""
from answers.users.download_answers import load_answer_for_user, \
                                           path_for_urls, \
                                           path_for_button_names, \
                                           path_for_users_answers
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Dispatcher, Router, Bot, F
from aiogram.enums import ParseMode
from db_api import Database_async
from config import TOKEN_BOT
from loguru import logger
from pathlib import Path
import aiosqlite
import asyncio


bot = Bot(token=TOKEN_BOT, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
router_for_start_action = Router()
router_for_catalog = Router()

router_for_start_action.message.filter(F.chat.type == "private")
router_for_catalog.message.filter(F.chat.type == "private")


db_path = Path('db_api', 'database', 'shop_database.db')
db = Database_async(db_path=db_path)

logger.add('logs/logs.json',
           level='DEBUG',
           format='{time} {level} {message}',
           rotation='10 MB',
           compression='zip',
           serialize=True)


all_urls: dict = load_answer_for_user(path_for_file=
                                      path_for_urls)
button_names: dict = load_answer_for_user(path_for_file=
                                          path_for_button_names)
all_answer_for_user: dict = load_answer_for_user(path_for_file=
                                                 path_for_users_answers)
#оставил для себя как напоминание что можно
#по другому запускать цикл событий
#async def create_needs_tables():
#    await db.create_table_device_category()

try:
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(db.create_table_device_category()),
             loop.create_task(db.create_table_manufacturer()),
             loop.create_task(db.create_table_devices())]
    wait_tasks = asyncio.wait(tasks)
    loop.run_until_complete(wait_tasks)
    #asyncio.run(create_needs_tables())
except aiosqlite.OperationalError as sql_error:
    logger.error(sql_error)
except Exception as all_error:
    logger.error(all_error)
