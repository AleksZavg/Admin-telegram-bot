from typing import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.admin_choose_input import admin_choose_input_kb
from keyboards.default.yes_no import yes_or_no_kb
from keyboards.default.admin_panel import admin_panel_kb
from keyboards.default.after_start import after_start_kb
from middlewares.states.admin_panel_states import *
from utils.db_api import sql

from loader import dp

'''
data = {"username": "",
        "telegram_id": "", # int 
        "phone": "",
        "data_add": ""}
'''


@dp.message_handler(Text(equals=["Предоставить доступ", "Удалить доступ", "Проверить доступ", "Все, у кого есть доступ", "Формы для заполнения", "Подробно о пользователе", "Назад"]), state=None)
async def admin(message: types.Message):
    if message.text == "Предоставить доступ":
        await message.answer("Выберите способ ввода", reply_markup=admin_choose_input_kb)
        await write_user.step1.set()
    elif message.text == "Назад":
        await message.answer("Вы вышли из панели администатора", reply_markup=after_start_kb)
    elif message.text == "Удалить доступ":
        await message.answer("Введите Telegram ID пользователя, которого нужно удалить")
        await remove_user.step1.set()
    elif message.text == "Проверить доступ":
        await message.answer("Введите Telegram ID пользователя, которого нужно проверить")
        await check_user.step1.set()
    elif message.text == "Подробно о пользователе":
        await message.answer("Введите Telegram ID пользователя, о котором нужна доп. инфа")
        await all_info.step1.set()
    elif message.text == "Все, у кого есть доступ":
        res = await sql.all_from_base()
        temp_str = "⁣⁣⁣⁣⁣⁣⁣+ | Username - Telegram ID\n"
        temp_str += "---|-----------------------------------------------\n"
        num = 1
        for temp in res:
            temp_str += f"{num} |  {temp[0]}  -  {temp[1]} \n"
            num += 1
        await message.answer(temp_str)


