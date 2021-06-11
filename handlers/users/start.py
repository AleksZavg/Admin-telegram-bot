from typing import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from keyboards.default.after_start import after_start_kb

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Приветики", reply_markup=after_start_kb)
    await message.answer_sticker("CAACAgIAAxkBAAECaLxgwdkd0VAsZfZbK94vR1LU1MgNiQAC7AADAexmGqwgu7-uFm-tHwQ")
