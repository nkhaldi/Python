from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext

import inline
from states import Location


async def call_ask_location(callback: types.CallbackQuery):
    await callback.message.answer("Укажите новую локацию /set_location")


async def cmd_ask_location(message: types.Message):
    ask = "Локация не указана."
    ask += "Укажите локацию после комманды /set_location"
    await message.answer(ask)


async def get_location(state: FSMContext):
    async with state.proxy() as data:
        location = data['location']
    return location


async def set_location(message: types.Message):
    await message.answer("Укажите новую локацию")
    await Location.location.set()


async def answer_location(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(location=answer)
    await message.answer(f"Новая локация: {answer}", reply_markup=inline.WEATHER)


def register_location(dp: Dispatcher):
    dp.register_message_handler(set_location, commands=['set_location'], state='*')
    dp.register_message_handler(answer_location, content_types=types.ContentTypes.TEXT, state=Location.location)

    dp.register_message_handler(cmd_ask_location, content_types=types.ContentTypes.ANY)
    dp.register_callback_query_handler(call_ask_location)
