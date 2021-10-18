import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}"
        )
        data = r.json()
        pprint(data)
    except Exception as ex:
        print(ex)
        print("Has the government changed the name of the city?")


def main():
    city = 'Almaty'
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
