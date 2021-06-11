from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_panel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Предоставить доступ"),
            KeyboardButton("Удалить доступ")
        ],
        [
            KeyboardButton("Проверить доступ"),
            KeyboardButton("Подробно о пользователе")
        ],
        [
            KeyboardButton("Формы для заполнения"),
            KeyboardButton("Все, у кого есть доступ")
        ],
        [
            KeyboardButton("Назад")
        ]
    ], 
    resize_keyboard=True
)