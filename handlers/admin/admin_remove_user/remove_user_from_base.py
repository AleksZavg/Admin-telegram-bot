from typing import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.admin_panel import admin_panel_kb
from middlewares.states.admin_panel_states import remove_user
from utils.db_api import sql

from loader import dp

'''
data = {"username": "",
        "telegram_id": "", # int 
        "phone": "",
        "data_add": ""}
'''

@dp.message_handler(text="/cancel", state="*")
async def back(message: types.Message, state: FSMContext):
    await message.answer("Действие отменено!", reply_markup=admin_panel_kb)
    await state.finish()

@dp.message_handler(state=remove_user.step1)
async def first_step(message: types.Message, state: FSMContext):
    data = {"telegram_id": int(message.text)}
    res = await sql.delete(data)
    if res == "User is not in the base":
        await message.answer("Пользователя нет в базе")
        await state.finish()
    elif res == "Succeed delete":
        await message.answer("Успешно!")
        await state.finish()
    elif res == "You can not delete admin":
        await message.answer("Вы не можете удалить себя!")
        await state.finish()
    