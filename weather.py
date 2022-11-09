import requests
from pprint import pprint

city=input('Enter your city :')

url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=581be37c407e46987bef42f3e9ef6abd&unit=metric'.format(city)

res = requests.get(url)

data=res.json()

temp = data['main']['temp']
wind_speed=data['wind']['speed']
latitude=data['coord']['lat']
longitude=data['coord']['lon']

description =data['weather'][0]['description']

print('Temperature: {} degree celcius'.format(temp))
print('wind speed:{} m/s'.format(wind_speed))
print('Longitude:{}'.format(longitude))
print('Latitude:{}'.format(latitude))
print('Description:{}'.format(description))