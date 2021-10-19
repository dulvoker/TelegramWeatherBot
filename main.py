import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        pprint(data)



        city_name = data['name']
        wind_speed = data['wind']['speed']
        weather_mood = data['weather'][0]['main']
        current_temp = data['main']['temp']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        local_time = data['dt']
        local_time = datetime.datetime.fromtimestamp(local_time)
        # local_date = local_time.strftime("%Y-%m-%d")
        # local_time = local_time.strftime("%H:%M:%S")
        sunrise = datetime.datetime.fromtimestamp(sunrise)
        sunset = datetime.datetime.fromtimestamp(sunset)
        sunrise = sunrise.strftime("%H:%M:%S")
        sunset = sunset.strftime("%H:%M:%S")


        # print(f"Date:  {local_date}\n"
        #       f"City:  {city_name}\n"
        #       f"Local time:  {local_time}\n"
        #       f"Weather mood: {weather_mood}\n"
        #       f"Current temperature:  {current_temp}°C\n"
        #       f"Temperature varies from {temp_min}°C to {temp_max}°C\n"
        #       f"Sunrise: {sunrise}, Sunset: {sunset}\n"
        #       f"Wind speed: {wind_speed} m/s")
    except Exception as ex:
        print(ex)
        print("Has the government changed the name of the city?")


def main():
    city = input("Enter the city name: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
