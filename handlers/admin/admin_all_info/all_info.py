from typing import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.admin_panel import admin_panel_kb
from middlewares.states.admin_panel_states import all_info
from utils.db_api import sql

from loader import dp

@dp.message_handler(text="/cancel", state="*")
async def back(message: types.Message, state: FSMContext):
    await message.answer("Действие отменено!", reply_markup=admin_panel_kb)
    await state.finish()

@dp.message_handler(state=all_info.step1)
async def first_step(message: types.Message, state: FSMContext):
    data = {"telegram_id": message.text}
    res = await sql.all_info(data)
    if res == "User is not in the base":
        await message.answer("Пользователя нет в базе")
        await state.finish()
    elif res != "User is not in the base":
        temp_str = "Данные, которые есть в базе:\n"
        temp_str += f"1) Username -  {res[0]}\n2) Telegram ID -  {res[1]}\n3) Phone -  {res[2]}\n4) Data add -  {res[3]}\n"
        await message.answer(temp_str)
        await state.finish()
