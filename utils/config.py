import json
import os

with open('config.json') as f:
    CONFIG = json.load(f)

GREENAPI_INSTANCE = os.environ['GREENAPI_INSTANCE']
GREENAPI_API_KEY = os.environ['GREENAPI_API_KEY']
CHAT_ID = os.environ['CHAT_ID']
RAIN_THRESOLD = CONFIG['rain_thresold']
