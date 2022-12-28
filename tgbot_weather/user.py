from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    greeting = f"<b>Привет, {message.from_user.first_name}!</b>\n"
    greeting += "Укажи город"
    await message.reply(greeting)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
