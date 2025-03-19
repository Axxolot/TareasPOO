
import  requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
            'q': city,
            'appid': api_key,
            'units' : metric
    }
    response = requests.get(base_url, params=params)
    return data
city = 'Toluca'
weather = get_weather(api_key, city)
print(weather)

