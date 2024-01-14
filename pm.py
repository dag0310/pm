#!/usr/bin/python3

import os
import configparser
import json
import requests
import time
from datetime import datetime
from dateutil import tz
import simple_sds011

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

pm = simple_sds011.SDS011(config['general']['device'])
pm.active = 1
pm.mode = simple_sds011.MODE_PASSIVE
time.sleep(int(config['general']['init_sleep_seconds']))
date = datetime.now(tz.tzlocal()).isoformat()
pm_values = pm.query()
pm25 = pm_values['value']['pm2.5']
pm10 = pm_values['value']['pm10.0']
pm.active = 0

url = config['general']['api_url']
data = { 'fields': [date, pm25, pm10] }
headers = { 'Content-Type': 'application/json' }

requests.post(url, data=json.dumps(data), headers=headers)
