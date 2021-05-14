
from .models import Device
from Adafruit_IO import MQTTClient
from .weatherinfo import get_weatherinfo, update_weatherinfo
import sys

# Subscribe to devices


ADAFRUIT_IO_USERNAME = 'hugholousk'
ADAFRUIT_IO_KEY = 'aio_Uzwb85BFHHZO1gEeO6wbpNKGoUCY'


class DeviceConnector():

    def __init__(self, key_id: str):
        self.key_id = key_id
    # Define callback functions which will be called when certain events happen.

    def subscribe(self):
        def connected(client):
            print(
                'Connected to Adafruit IO!  Listening for {0} changes...'.format(self.key_id))
            client.subscribe(self.key_id)

        def subscribe(client, userdata, mid, granted_qos):
            print('Subscribed to {0} with QoS {1}'.format(
                self.key_id, granted_qos[0]))

        def disconnected(client):
            print('Disconnected from Adafruit IO!')
            sys.exit(1)

        def message(client, feed_id, payload):
            print('Feed {0} received new value: {1}'.format(feed_id, payload))
            # Update device database
            print('Update database ...')
            Device.objects.filter(key=feed_id).update(value=payload)
            # Update weather info
            update_weatherinfo()
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


for (i, deviceQuery) in enumerate(Device.objects.all()):
    DeviceConnector(deviceQuery.__dict__['key']).subscribe()

# map(lambda deviceQuery: DeviceConnector(
#     deviceQuery.__dict__['key']).subscribe(), Device.objects.all())

# Device.objects.filter(key='bk-iot-light-0').update(value=111)
