from typing import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.yes_no import yes_or_no_kb
from keyboards.default.admin_panel import admin_panel_kb
from middlewares.states.admin_panel_states import write_user
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


@dp.message_handler(state=write_user.step1)
async def first_step(message: types.Message, state: FSMContext):
    await state.update_data(way_input=message.text)
    temp = await state.get_data()
    if temp["way_input"] == "Быстрый":
        await message.answer("Введите полный запрос\n(username|telegramID|phone|data_add\nЕсли некоторых данных нет,\nто подставьте в них - empty)")
        await write_user.step2.set()
    elif temp["way_input"] == "Медленный":
        await message.answer("Введите username пользователя, которого нужно добавить\n(Если некоторых требуемых данных - нет, то подставьте в них - empty)")
        await write_user.step2.set()


@dp.message_handler(state=write_user.step2)
async def second_step(message: types.Message, state: FSMContext):
    if "|" in message.text:
        temp = message.text.split("|")
        data = {"username": temp[0],"telegram_id": int(temp[1]), "phone": temp[2], "data_add": temp[3]}
        res = await sql.write(data)
        if res == "User is in the base":
            await message.answer("Этот пользователь уже есть в базе", reply_markup=admin_panel_kb)
            await state.finish()
        elif message.text == "Succeed write":
            await message.answer("Успешно!", reply_markup=admin_panel_kb)
            await state.finish()
    elif message.text not in ["Медленный", "Быстрый"]:
        await state.update_data(username=message.text)
        await message.answer("Введите Telegram ID пользователя, которого нужно добавить")
        await write_user.step3.set()
    else:
        await message.answer("Введите корректные данные")


@dp.message_handler(state=write_user.step3)
async def third_step(message: types.Message, state: FSMContext):
    await state.update_data(telegram_id=message.text)
    await message.answer("Введите телефон пользователя, которого нужно добавить (вместе с +)")
    await write_user.step4.set()


@dp.message_handler(state=write_user.step4)
async def four_step(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите текущую дату в формате ДД.ММ.ГОД (22.06.2021)")
    await write_user.step5.set()


@dp.message_handler(state=write_user.step5)
async def five_step(message: types.Message, state: FSMContext):
    await state.update_data(data_add=message.text)
    temp = await state.get_data()
    data = {"username": temp["username"],
            "telegram_id": temp["telegram_id"],
            "phone": temp["phone"],
            "data_add": temp["data_add"]}
    await message.answer(f"Username - {data['username']}\nTelegram ID - {data['telegram_id']}\nPhone - {data['phone']}\nData add - {data['data_add']}\n\nВы верно ввели данные?", reply_markup=yes_or_no_kb)
    await write_user.step6.set()


@dp.message_handler(state=write_user.step6)
async def six_step(message: types.Message, state: FSMContext):
    if message.text == "Нет":
        await state.reset_state()
        await message.answer("Введите username пользователя, которого нужно добавить\n(Если некоторых требуемых данных - нет,\nто подставьте в них - empty)")
        await state.reset_state()
        await write_user.step2.set()
    elif message.text == "Да":
        temp = await state.get_data()
        data = {"username": temp["username"], "telegram_id": int(temp["telegram_id"]), "phone": temp["phone"], "data_add": temp["data_add"]}
        res = await sql.write(data)
        if res == "User is in the base":
            await message.answer("Этот пользователь уже есть в базе", reply_markup=admin_panel_kb)
            await state.finish()
        elif message.text == "Succeed write":
            await message.answer("Успешно!", reply_markup=admin_panel_kb)
            await state.finish()
