#!/usr/bin/env python3

# Head or Tail Telegram bot
# @Head_or_Tail_Bot
# http://t.me/Head_or_Tail_Bot


from random import randrange

import telebot
from telebot.types import ReplyKeyboardMarkup as keyboard

token_file = open("/Users/narek/.pass/.head_or_tail.token")
token = token_file.read().rstrip("\n")
bot = telebot.TeleBot(token)

board = keyboard(True, True)
board.row("Flip")


@bot.message_handler(commands=["start"])
def start(message):
    greeting = f"<b>Hello, {message.from_user.first_name}!</b>\nLet's play!"
    bot.send_message(message.chat.id, greeting, parse_mode="html", reply_markup=board)


@bot.message_handler(content_types=["text"])
def mess(message):
    input_message = message.text.strip().lower()
    if input_message == "flip":
        rand = randrange(2)
        msg = "Head" if rand else "Tails"

        bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=board)


bot.polling(none_stop=True)
