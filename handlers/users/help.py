from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

@dp.message_handler(text="Список команд")
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Запустить бота",
            "/admin - Панель управления администратора",
            "/info - Информация о боте (от автора-разработчика)",
            "/help - Вывести справку", 
            "/cancel - Остановить текущее действие")
    
    await message.answer("\n".join(text))
