from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import logging

from data.data import HELP_COMMAND, START_MESSAGE

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)   # написать сообщение текст
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=START_MESSAGE, parse_mode='HTML')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
