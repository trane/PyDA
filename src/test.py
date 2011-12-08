#!/usr/local/bin/python3
import json
from pprint import pprint

json_data = open('sample.pyda')
pyda_struct = json.load(json_data)
pprint(pyda_struct)
json_data.close()
