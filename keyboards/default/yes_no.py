from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yes_or_no_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Да"),
            KeyboardButton("Нет")
        ]
    ], 
    resize_keyboard=True
)