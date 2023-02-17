from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from config import TOKEN_API
import logging
from keyboards import start_kb, kb_principle
from aiogram.dispatcher.filters import Text
from data.data import HELP_COMMAND, START_MESSAGE, ABOUT_MESSAGE, Principles

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print("Bot start")


# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text=HELP_COMMAND)  # написать сообщение текст
#     await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=START_MESSAGE,
                           parse_mode='HTML',
                           reply_markup=start_kb)
    await message.delete()


@dp.message_handler(Text(equals="Теория тестирования"))
async def get_theory_button(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Получение теории тестирования",
                           reply_markup=kb_principle)
    await message.delete()


@dp.message_handler(Text(equals='2 принцип'))
async def get_2_principle(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=Principles.TWO_PRINCIPE,
                           reply_markup=kb_principle)
    await message.delete()


@dp.message_handler(Text(equals='Главное меню'))
async def get_main_menu(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в главное меню",
                           reply_markup=start_kb)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
