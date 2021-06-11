from typing import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from keyboards.default.after_start import after_start_kb

from loader import dp

@dp.message_handler(text="Общедоступные функции")
async def public_func(message: types.Message):
    await message.answer("Пока не работает")
