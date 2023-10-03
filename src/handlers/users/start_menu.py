from aiogram.utils.markdown import hunderline, hlink, hbold
from loader import router_for_start_action
from answers import all_answer_for_user
from aiogram.filters import Command
from aiogram import types


@router_for_start_action.message(Command("start"))
async def start_work_bot(message: types.Message):
    text: str = f'Здраствуйте, ' \
                f'{hbold(message.from_user.first_name)}! '\
                f'Это {hunderline("ПЕДПРОЕКТ")} !\n'\
                f'Добро пожаловать в наш магазин ! ' \
                f'В каталоге товаров представлены ' \
                f'модели на которые можно ' \
                f'{hunderline("оформить заказ")} !\n' \
                f'Мой ➡️ ' \
                f'{hlink( url= r"https://t.me/Fedor_Sannikov", title="создатель")}.\n\n' \
                f'Меню бота: \n\n' \
                f'/start - Начало работы;\n' \
                f'/catalog - Просмотр каталога товаров;\n' \
                f'/help - Список комманд доступных пользователю.\n'\
                f'\n\n'
    await message.answer(text=text)


@router_for_start_action.message(Command("help"))
async def give_all_commands_for_users(message: types.Message):
    text: str = ''
    for command, description in \
            all_answer_for_user['all_commands_for_users'].items():
        text += command + ' - ' + description + '\n'
    await message.answer(text=text)