#!/usr/bin/env python3

import requests


def get_coords():
    return 40.15, 44.47


def get_api_url(lat, lon):
    api_key_file = open('/Users/narek/.pass/.openweather')
    api_key = api_key_file.read().rstrip('\n')

    api_host = "https://api.openweathermap.org/data/2.5/weather"
    api_params = f"units=metric&lat={lat}&lon={lon}&appid={api_key}"
    api_url = f"{api_host}?{api_params}"

    return api_url


def get_weather(lat, lon):
    api_url = get_api_url(lat, lon)
    resp = requests.get(api_url)
    weather_json = resp.json()
    return weather_json


lat, lon = get_coords()
weather = get_weather(lat, lon)
