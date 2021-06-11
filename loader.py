from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage

from data import config

bot = Bot(token=config.data["api_key"], parse_mode=types.ParseMode.HTML)
storage = MongoStorage(host='localhost', port=27017, db_name='admin_telegram_bot_FSM')
dp = Dispatcher(bot, storage=storage)
