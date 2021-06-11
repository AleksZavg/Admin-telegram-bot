from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_choose_input_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Быстрый"),
            KeyboardButton("Медленный")
        ]
    ], 
    resize_keyboard=True
)