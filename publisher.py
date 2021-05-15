from Adafruit_IO import MQTTClient, Client, Data
import sys
import random
import time
import json
ADAFRUIT_IO_USERNAME = 'hugholousk'
ADAFRUIT_IO_KEY = 'aio_tEor43A3JQNwrenJLIKpBo9XzQAN'
FEED_ID = 'bk-iot-light'

# Create an MQTT client instance.
client = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


while True:
    value = random.randint(0, 100)
    data = Data(value=json.dumps({
        "id": "1",
        "name": "LIGHT",
        "data": value,
        "unit": ''
    }))
    print('Pushing data')
    client.create_data('bk-iot-light', data)
    time.sleep(3)
