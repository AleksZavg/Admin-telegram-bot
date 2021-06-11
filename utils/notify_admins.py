import logging, time

from aiogram import Dispatcher

from data.config import data


async def on_startup_notify(dp: Dispatcher):
    for admin in data["who_need_notify"]:
        try:
            await dp.bot.send_message(admin, f"❗️ [{time.strftime('%m/%d/%Y, %H:%M:%S')}] - Я была перезагружена!")
            # 12/07/2019, 15:01:09 - что выдаст
            await dp.bot.send_sticker(admin, "CAACAgIAAxkBAAECaKhgwdTtsNAlX5VkuSSA-2Gax_DGOgAC9QADAexmGk1IYGxz6uPMHwQ")

        except Exception as err:
            logging.exception(err)
