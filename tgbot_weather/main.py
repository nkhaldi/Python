#!/usr/bin/env python3

# Head or Tail Telegram bot
# @nkhaldi_weather_bot
# https://t.me/nkhaldi_weather_bot


from aiogram import Bot


token_file = open('/Users/narek/.pass/.weather.token')
token = token_file.read().rstrip('\n')
bot = Bot(token=token)
