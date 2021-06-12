from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

private_func_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Узнать геолокацию пользователя"),
            KeyboardButton("temp")
        ],
        [
            KeyboardButton("temp"),
            KeyboardButton("temp")
        ],
        [
            KeyboardButton("Назад")
        ]
    ], 
    resize_keyboard=True
)