from aiogram import Dispatcher
from aiogram.types import Message

import inline


async def user_start(message: Message):
    greeting = f"<b>Привет, {message.from_user.first_name}!</b>\n"
    greeting += "Укажи город"
    await message.reply(greeting, reply_markup=inline.HELP)


async def user_help(message: Message):
    help = 'Help!'
    await message.reply(help, reply_markup=inline.HELP)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
