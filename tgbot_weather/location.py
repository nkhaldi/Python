import requests
from environs import Env

from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext

from tgbot.keyboards import inline
from tgbot.states.location import Location


env = Env()
env.read_env(".env")


def get_crd_api_url(location):
    api_key = env.str("GEO_API_KEY")
    api_host = env.str("GEO_API_HOST")
    api_params = f"apikey={api_key}&format=json&geocode={location}"
    # https://geocode-maps.yandex.ru/1.x/?apikey=ваш API-ключ&format=json&geocode=Тверская+6
    # порядок параметров не важен
    api_url = api_host + "?" + api_params
    return api_url


def get_coordinates(location):
    api_url = get_crd_api_url(location)
    response = requests.get(api_url)
    crd_json = response.json()
    try:
        geobj = crd_json["response"]["GeoObjectCollection"]["featureMember"][0]
        coordinates = geobj["GeoObject"]["Point"]["pos"]
    except:
        coordinates = False
    return coordinates


async def call_ask_location(callback: types.CallbackQuery):
    await callback.message.answer('Укажите новую локацию /set_location')


async def cmd_ask_location(message: types.Message):
    await message.answer('Укажите новую локацию /set_location')


async def get_location(state: FSMContext):
    async with state.proxy() as data:
        location = data['location']
    return location


async def set_location(message: types.Message):
    await message.answer('Укажите новую локацию')
    await Location.location.set()


async def answer_location(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(location=answer)
    await message.answer(f"Новая локация: {answer}", reply_markup=inline.WEATHER)


def register_location(dp: Dispatcher):
    dp.register_message_handler(set_location, commands=["set_location"], state="*")
    dp.register_message_handler(answer_location, content_types=types.ContentTypes.TEXT, state=Location.location)

    dp.register_message_handler(cmd_ask_location, content_types=types.ContentTypes.ANY)
    dp.register_callback_query_handler(call_ask_location)
