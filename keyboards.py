from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_theory = KeyboardButton('Теория тестирования')
button_about = KeyboardButton('/about')
start_kb.add(button_theory, button_about)

kb_principle = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='1 принцип: Исчерпывающее тестирование невозможно')
bp2 = KeyboardButton(text='2 принцип: Тестирование демонстрирует наличие дефектов, а не их отсутствие')
bp3 = KeyboardButton(text='3 принцип: Заблуждение об отсутствии ошибок')
bp4 = KeyboardButton(text='4 принцип: Раннее тестирование сохраняет время и деньги')
bp5 = KeyboardButton(text='5 принцип: Принцип скопления или кластеризация дефектов')
bp6 = KeyboardButton(text='6 принцип: Тестирование зависит от контекста')
bp7 = KeyboardButton(text='7 принцип: Парадокс пестицида')
button_menu = KeyboardButton(text='Главное меню')

kb_theory = ReplyKeyboardMarkup(resize_keyboard=True)

kb_principle.add(bp1).add(bp2).add(bp3).add(bp4).add(bp5).add(bp6).add(bp7).add(button_menu)
