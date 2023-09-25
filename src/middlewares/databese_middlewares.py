from aiogram import BaseMiddleware
from aiogram import types
#from loader import db


class GetDeviceCategory(BaseMiddleware):

    async def on_pre_process_message(self,
                                 message: types.Message,
                                 data: dict):
        pass

        #print(await db.info_all_device_category())