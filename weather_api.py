import requests

def get_weather_data(city):
    API_KEY = '3030f7a9a6dad3faff2e6cf8ad9beba4'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        data = requests.get(url).json()
        # print(data)
        description = data['weather'][0]['description']
        temperature = int(data['main']['temp']) - 273.15
        real_feel = int(data['main']['feels_like']) - 273.15
        print(f'City: {city}; description: {description}; temp: {round(temperature, 2)}'
              f';feels like: {round(real_feel,2)}')
    except KeyError as e:
        print(f'An error occured. The follwing key does not exist: {e}\n'
              f'Please check the API URL')


if __name__ == '__main__':
    city = input('city: ')
    get_weather_data(city)