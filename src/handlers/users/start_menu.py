from aiogram.utils.markdown import hunderline, \
                                   hlink, \
                                   hbold
from loader import router_for_start_action
from aiogram.filters import Command
from aiogram import types


@router_for_start_action.message(Command("start"))
async def start_work_bot(message: types.Message):
    text: str = f'Здраствуйте, ' \
                f'{hbold(message.from_user.first_name)}.\n' \
                f'Добро пожаловать в наш магазин ! ' \
                f'В каталоге товаров представлены ' \
                f'модели на которые можно ' \
                f'{hunderline("оформить заказ")} !\n' \
                f'Мой ➡️ ' \
                f'{hlink( url= r"https://t.me/Fedor_Sannikov", title="создатель")}.\n' \
                f'Меню бота: \n\n' \
                f'/catalog - Просмотр каталога товаров' \
                f'\n\n'
    await message.answer(text=text)
