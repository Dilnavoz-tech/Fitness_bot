from aiogram import executor
import logging
from bot.dispatcher import dp

from bot.handlers import start_handler


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
