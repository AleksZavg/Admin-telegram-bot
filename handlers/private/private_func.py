from typing import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from keyboards.default.admin_panel import admin_panel_kb
from keyboards.default.private_func import private_func_kb
from utils.db_api import sql
from middlewares.states.private_func import learn_geolocation

from loader import dp

@dp.message_handler(state=None)
async def main(message: types.Message, data):
    res = await sql.all_info(data)
    await message.answer(f"Добрый день, {res[0]}", reply_markup=private_func_kb)
    
@dp.message_handler(text=["Узнать геолокацию пользователя"], state=None)
async def private_hander(message: types.Message):
    if message.text == "Узнать геолокацию пользователя":
        await message.answer("Введите Telegram ")
        await learn_geolocation.step1.set()
