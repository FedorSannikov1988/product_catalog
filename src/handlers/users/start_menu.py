"""
Starting (getting started) with a telegram bot.
"""
from loader import router_for_start_action, all_answer_for_user
from aiogram.utils.markdown import hunderline, hlink, hbold
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import types


@router_for_start_action.message(Command("start"))
async def start_work_bot(message: types.Message,
                         state: FSMContext):
    """
    Response to the start command.

    :param message: types.Message
    :param state: FSMContext
    :return: None
    """
    await state.clear()

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
    """
    Response to the help command .
    Displays a list of all commands .

    :param message: types.Message
    :return: None
    """
    text: str = ''
    for command, description in \
            all_answer_for_user['all_commands_for_users'].items():
        text += command + ' - ' + description + '\n'
    await message.answer(text=text)