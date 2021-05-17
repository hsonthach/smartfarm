
from .models import Device
from Adafruit_IO import MQTTClient
from .weatherinfo import get_weatherinfo, update_weatherinfo
import sys
import json

# Subscribe to devices
from dotenv import dotenv_values
config = dotenv_values(".env")
ADAFRUIT_IO_USERNAME = config['ADAFRUIT_IO_USERNAME']
ADAFRUIT_IO_KEY = config['ADAFRUIT_IO_KEY']
print(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


class DeviceConnector():

    def __init__(self, feed_id: str):
        self.feed_id = feed_id
    # Define callback functions which will be called when certain events happen.

    def subscribe(self):
        def connected(client):
            print(
                'Connected to Adafruit IO!  Listening for {0} changes...'.format(self.feed_id))
            client.subscribe(self.feed_id)

        def subscribe(client, userdata, mid, granted_qos):
            print('Subscribed to {0} with QoS {1}'.format(
                self.feed_id, granted_qos[0]))

        def disconnected(client):
            print('Disconnected from Adafruit IO!')
            sys.exit(1)

        def message(client, feed_id, payload):
            print('Feed {0} received new value: {1}'.format(feed_id, payload))
            # Update device database
            print('Update database ...')
            res = json.loads(payload)
            device = Device(id=str(
                res["id"]), data=res["data"], name=res["name"], unit=res["unit"])
            device.save()
            print('Data updated')
            # Device.objects.filter(id=device["id"]).update(data=device["data"], name=device["name"], unit=device["unit"]))
            # Update weather info
            # update_weatherinfo()
            # TODO: Handle value change event ( > 100, < 100)

        # Create an MQTT client instance.
        client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

        # Setup the callback functions defined above.
        client.on_connect = connected
        client.on_disconnect = disconnected
        client.on_message = message
        client.on_subscribe = subscribe

        # Connect to the Adafruit IO server.
        client.connect()

        client.loop_background()


# a = DeviceConnector('bk-iot-light-0')
# a.execute()

feeds = ['bk-iot-light', 'bk-iot-soil', 'bk-iot-temp-humid']
for (i, feed_id) in enumerate(feeds):
    DeviceConnector(feed_id).subscribe()
# for (i, deviceQuery) in enumerate(Device.objects.all()):
#     DeviceConnector(deviceQuery.__dict__['id']).subscribe()

# map(lambda deviceQuery: DeviceConnector(
#     deviceQuery.__dict__['key']).subscribe(), Device.objects.all())

# Device.objects.filter(key='bk-iot-light-0').update(value=111)
