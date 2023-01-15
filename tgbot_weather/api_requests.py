import requests
from environs import Env
from enum import IntEnum
from datetime import datetime


env = Env()
env.read_env('.env')


class WindDirection(IntEnum):
    северный = 0
    северовосточный = 45
    восточный = 90
    юговосточный = 135
    южный = 180
    югозападный = 225
    запажный = 270
    северозападный = 315


def get_wt_api_url(location):
    coordinates = get_coordinates(location)
    if not coordinates:
        return False

    api_host = env.str('WT_API_HOST')
    api_key = env.str('WT_API_KEY')
    lon, lat = coordinates.split(' ')

    api_params = f'units=metric&lat={lat}&lon={lon}&appid={api_key}'
    api_url = api_host + '?' + api_params
    return api_url


def get_wind_direction(degrees):
    degrees = round(degrees / 45) * 45
    if degrees == 360:
        degrees = 0

    return WindDirection(degrees).name


def get_temperature(location):
    api_url = get_wt_api_url(location)
    if not api_url:
        return "Неизвестное местоположение, введите заново"

    response = requests.get(api_url)
    wt_json = response.json()

    temp = wt_json['main']['temp']
    feels = wt_json['main']['feels_like']

    msg = f"Температура на данный момент составляет {temp}°C.\n"
    msg += f"Ощущается как {feels}°C."
    return msg


def get_wind(location):
    api_url = get_wt_api_url(location)
    if not api_url:
        return "Неизвестное местоположение, введите заново"

    response = requests.get(api_url)
    wt_json = response.json()

    direction = get_wind_direction(wt_json['wind']['deg'])
    speed = wt_json['wind']['speed']

    msg = f"Ветер {direction}, cкорость {speed} м/с."
    return msg


def get_suntime(location):
    api_url = get_wt_api_url(location)
    if not api_url:
        return "Неизвестное местоположение, введите заново"

    response = requests.get(api_url)
    wt_json = response.json()

    sunrise_ts = datetime.fromtimestamp(wt_json['sys']['sunrise'])
    sunset_ts = datetime.fromtimestamp(wt_json['sys']['sunset'])
    sunrise = sunrise_ts.strftime('%H:%M')
    sunset = sunset_ts.strftime('%H:%M')

    msg = f"Восход солнца в {sunrise}, закат солнца в {sunset}."
    return msg


def get_crd_api_url(location):
    api_key = env.str('GEO_API_KEY')
    api_host = env.str('GEO_API_HOST')
    api_params = f'apikey={api_key}&format=json&geocode={location}'
    api_url = api_host + '?' + api_params
    return api_url


def get_coordinates(location):
    api_url = get_crd_api_url(location)
    response = requests.get(api_url)
    crd_json = response.json()
    try:
        geobj = crd_json['response']['GeoObjectCollection']['featureMember'][0]
        coordinates = geobj['GeoObject']['Point']['pos']
    except:
        coordinates = False

    return coordinates
