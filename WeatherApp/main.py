import requests
import json
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=01c7974cc345411484c90549232703&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
f = wdic["current"]["temp_f"]
speaker.Speak(f"The current weather of {city} is {w} degree celsius and {f} degree fehrenhite")