from Adafruit_IO import MQTTClient, Client, Data
import sys
import random
import time
import json
ADAFRUIT_IO_USERNAME = 'hugholousk'
ADAFRUIT_IO_KEY = 'aio_tEor43A3JQNwrenJLIKpBo9XzQAN'

# Create an MQTT client instance.
client = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

feeds = ['bk-iot-light', 'bk-iot-soil', 'bk-iot-temp-humid']
feeds = [
    {
        "name": 'bk-iot-light',
        "payload": {
            "id": "1",
            "name": "LIGHT",
            "data": 0,
            "unit": ''
        }
    },
    {
        "name": 'bk-iot-soil',
        "payload": {
            "id": "2",
            "name": "SOIL",
            "data": 0,
            "unit": ''
        }
    },
    {
        "name": 'bk-iot-temp-humid',
        "payload": {
            "id": "3",
            "name": "TEMP-HUMID",
            "data": '0-0',
            "unit": ''
        }
    }
]
while True:
    value = random.randint(0, 200)
    random_feed = feeds[random.randint(0, 2)]
    if (random_feed['name'] == 'bk-iot-temp-humid'):
        random_feed['payload']['data'] = str(random.randint(20, 40)) + '-' + str(
            value)
    else:
        random_feed['payload']['data'] = value
    print('Pushing data')
    print(random_feed)
    data = Data(value=json.dumps(random_feed['payload']))
    client.create_data(random_feed['name'], data)
    time.sleep(3)
