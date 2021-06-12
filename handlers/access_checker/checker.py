from typing import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from keyboards.default.admin_panel import admin_panel_kb
from keyboards.default.private_func import private_func_kb
from utils.db_api import sql
from handlers.admin import admin_panel
from handlers.private import private_func

from loader import dp

data = {"username": "",
        "telegram_id": "", # int 
        "phone": "",
        "data_add": ""}

@dp.message_handler(Command("admin"))
async def access_checker(message: types.Message):
    data["telegram_id"] = message.from_user.id
    res = await sql.check(data)
    if res == "This is admin":
        await message.answer("Здравствуйте админ!", reply_markup=admin_panel_kb)
        await admin_panel.admin(message)
    elif res == "not in base": 
        await message.answer("В доступе отказано, вас нет в базе")
    elif res == "is in base":
        await message.answer("Вы не можете войти в панель администратора, но у вас есть доступ к приватным возможностям\nДля этого введите /private")


@dp.message_handler(Command("private"))
async def private(message: types.Message):
    data["telegram_id"] = message.from_user.id
    res = await sql.check(data)
    if res == "This is admin":
        pass
    elif res == "not in base":
        await message.answer("В доступе отказано, вас нет в базе")
    elif res == "is in base":
        await private_func.main(message, data)
