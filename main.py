from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API
import logging

from data.data import HELP_COMMAND, START_MESSAGE, ABOUT_MESSAGE

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_help = KeyboardButton('/help')
button_theory = KeyboardButton('/theory')
button_about = KeyboardButton('/about')
kb.add(button_help, button_theory, button_about)



ikb = InlineKeyboardMarkup(row_width=2)


async def on_startup(_):
    print("Bot start")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND)   # написать сообщение текст
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=START_MESSAGE,
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['about'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=ABOUT_MESSAGE,
                           parse_mode='HTML')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)

