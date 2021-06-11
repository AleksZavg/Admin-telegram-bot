from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("admin", "Панель управления администратора"),
            types.BotCommand("info", "Информация о боте (от автора-разработчика)"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("cancel", "Остановить текущее действие")
        ]
    )
