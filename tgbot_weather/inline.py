from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


BTN_TEMPERATURE = InlineKeyboardButton('Temperature', callback_data='temperature')
BTN_WIND = InlineKeyboardButton('Wind', callback_data='wind')
BTN_SUNTIME = InlineKeyboardButton('Suntime', callback_data='suntime')

WEATHER = InlineKeyboardMarkup().add(BTN_TEMPERATURE, BTN_WIND, BTN_SUNTIME)
TEMPERATURE = InlineKeyboardMarkup().add(BTN_WIND, BTN_SUNTIME)
WIND = InlineKeyboardMarkup().add(BTN_TEMPERATURE).add(BTN_SUNTIME)
SUNTIME = InlineKeyboardMarkup().add(BTN_TEMPERATURE, BTN_WIND)
