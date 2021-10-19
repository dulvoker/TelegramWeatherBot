import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="2066134351:AAGI0cjEN3-0V5FnW_Gg_gRGmXbf7bXs9-8")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.reply("Hi, send me the name of the city")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        city_name = data['name']
        wind_speed = data['wind']['speed']
        weather_mood = data['weather'][0]['main']
        current_temp = data['main']['temp']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        sunrise = datetime.datetime.fromtimestamp(sunrise)
        sunset = datetime.datetime.fromtimestamp(sunset)
        sunrise = sunrise.strftime("%H:%M:%S")
        sunset = sunset.strftime("%H:%M:%S")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        await message.reply(f"Date:  {current_date}\n"
                            f"City:  {city_name}\n"
                            f"Local time:  {current_time}\n"
                            f"Weather mood: {weather_mood}\n"
                            f"Current temperature:  {current_temp}°C\n"
                            f"Temperature varies from {temp_min}°C to {temp_max}°C\n"
                            f"Sunrise: {sunrise}, Sunset: {sunset}\n"
                            f"Wind speed: {wind_speed} m/s")
    except:
        await message.reply("I don't know such a city :(")


if __name__ == '__main__':
    executor.start_polling(dp)
