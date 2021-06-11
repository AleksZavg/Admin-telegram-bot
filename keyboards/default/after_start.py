from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

after_start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Список команд"),
            KeyboardButton("Общедоступные функции")
        ]
    ], 
    resize_keyboard=True
)