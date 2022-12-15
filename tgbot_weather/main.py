#!/usr/bin/env python3

# Head or Tail Telegram bot
# @nkhaldi_weather_bot
# https://t.me/nkhaldi_weather_bot


from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

token_file = open('/Users/narek/.pass/.weather.token')
token = token_file.read().rstrip('\n')

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    greeting = f"Првиет, {message.from_user.first_name}!\nКак погодка?"
    await message.reply(greeting)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("ПАМАГИТИ, Я В ТЕЛЕФОНЕ")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


executor.start_polling(dp)
