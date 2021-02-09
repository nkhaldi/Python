#!/usr/bin/env python3

# Head or Tail Telegram bot
# @Head_or_Tail_Bot
# http://t.me/Head_or_Tail_Bot


import telebot
from random import randrange


token_file = open('/home/narek/.pass/.head_or_tail.token')
token = token_file.read().rstrip('\n')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nСыграем?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message = message.text.strip().lower()
    if get_message == "орел" or get_message == "орёл":
        rand = 0
    elif get_message == "решка":
        rand = 1
    else:
        rand = randrange(2)

    if rand:
        msg = "Орёл"
    else:
        msg = "Решка"
    bot.send_message(message.chat.id, msg, parse_mode='html')


bot.polling(none_stop=True)
