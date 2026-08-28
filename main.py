import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

OWM_Endpoint = os.environ.get("OWM_ENDPOINT")
OWM_api_key = os.environ.get("OWM_API_KEY")

MY_LAT = 54.356030
MY_LONG = 18.646120


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWM_api_key,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=parameters)

weather_data = response.json()

will_rain = False

for day in weather_data["list"]:
    weather_code_info = day["weather"]
    weather_id_code = int(weather_code_info[0]["id"])
    if weather_id_code < 700:
        will_rain = True

if will_rain:
    message = "It will rain today! Bring an umbrella!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

    r = requests.get(url)
    print(r.json())
