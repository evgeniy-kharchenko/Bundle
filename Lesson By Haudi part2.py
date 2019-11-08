# Preperation
# Source of the weather metrics: https://openweathermap.org/
# Pre install module: pip install pyowm / Link: https://pypi.org/project/pyowm/
import pyowm

owm = pyowm.OWM('923ff2dd7610c6e377b0729187eb2c2d')

place = input("Choose your location: ")

# Search for current weather in region (Great Britain)
observation = owm.weather_at_place(place)
w = observation.get_weather()
print(w) 