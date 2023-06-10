import inline
from aiogram import Dispatcher
from aiogram.types import Message
from states import Location


async def user_start(message: Message):
    greeting = f"<b>Привет, {message.from_user.first_name}!</b>\n"
    greeting += "Укажите локацию"
    await message.reply(greeting)
    await Location.location.set()


async def user_help(message: Message):
    help = "Укажите локацию после комманды /set_location\n"
    help += "И выберите нужную метрику:\n"
    help += "/temperature - температура,\n"
    help += "/wind - скорость и направление ветра,\n"
    help += "/suntime - время восхода и заката солнца."
    await message.reply(help, reply_markup=inline.WEATHER)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_help, commands=["help"], state="*")
