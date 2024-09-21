from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="brasilia"):

  request_url = f'{os.getenv("API_URL")}?appid={os.getenv("API_KEY")}&q={city}&units=metric'

  print(request_url)

  weather_data = requests.get(request_url).json()

  return weather_data

if __name__ == "__main__":
  print('\n*** Get Weather Conditions **\n')

  city = input("\nProcure por uma Cidade: ")

  # weather_data =  get_current_weather(city)

  print("\n")
  pprint(weather_data)