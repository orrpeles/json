#!/bin/python
# Fetch weather data from command line using JSON

import sys, json, requests, pprint

# read requested location from command line
if len(sys.argv) < 2:
    print('enter a location to fetch weather from...')
    sys.exit()
location = ','.join(sys.argv[1:]) #join strings except the first

url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=aaa7e7b779dfa16b4073042d2a2d3047' % (location)
response = requests.get(url)
response.raise_for_status()

#print(response.text)

weatherData = json.loads(response.text)
pprint.pprint(weatherData)

#print(weatherData)

#w = weatherData['list']

