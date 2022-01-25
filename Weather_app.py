from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ua' 

owm = OWM( , config_dict)
mgr = owm.weather_manager()

place = input("В якому місті/країні? ")


observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print(f"В місті {place} зараз {w.detailed_status}")
print(f"Температура близько {temp} градусів")

if temp < 10:
  print("На вулиці холодно, де шапка?!")
elif temp <20:
  print("На вулиці досить прохолодно, накинь щось!")
else:
  print("На вулиці тепло, одягайся як тобі буде зручно!")
