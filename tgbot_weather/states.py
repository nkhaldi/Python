from aiogram.dispatcher.filters.state import State, StatesGroup


class Location(StatesGroup):
    location = State()
