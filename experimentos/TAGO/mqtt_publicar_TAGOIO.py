import time
import json
import paho.mqtt.client as paho
from paho import mqtt
from decouple import config, Csv
import random

client = paho.Client()

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set(config("TAGO_IO_USERNAME"), config("TAGO_IO_PASSWORD"))

client.connect(config("TAGO_IO_HOST"), 8883,keepalive=60)

#client.subscribe("sensor1", qos=0)
msg = [
                    {
                        'variable': 'sensor1',
                        'value'   :  random.randint(1000, 10000)
                    },
]

json_file = json.dumps(msg)

client.publish("tago/data/sensor1", payload=json_file, qos=1, retain=False)
