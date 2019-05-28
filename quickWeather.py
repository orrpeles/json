#!/bin/python
# Fetch weather data from command line using JSON

import sys, json, requests
# read requested location from command line
if len(sys.argv) < 2:
    print('enter a location to fetch weather from...')
    sys.exit()
location = ' '.join(sys.argv[1:]) #join strings except the first

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()


