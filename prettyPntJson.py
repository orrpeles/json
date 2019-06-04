#!/bin/python
# ref: https://stackoverflow.com/questions/23718896/pretty-print-json-in-python-pythonic-way
# ref: https://stackoverflow.com/questions/2835559/why-cant-python-parse-this-json-data

import json
from pprint import pprint

# cannot call json object like this: 'f = json.load('file')'
f = open('/home/enumtheworld/Documents/YoutubeGet-4b84683d255f.json')
data = json.load(f)
pprint(data)


