import time
import paho.mqtt.client as paho
from paho import mqtt
from decouple import config, Csv
import random

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="HIVEMQ", userdata=None, protocol=paho.MQTTv5)

client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set(config("HIVEMQ_USERNAME"), config("HIVEMQ_PASSWORD"))

# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(config("HIVEMQ_CLUSTER_URL"), config("HIVEMQ_PORT", cast=int))


# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
#client.subscribe("sensor1", qos=0)

# a single publish, this can also be done in loops, etc.
#client.publish("sensor1", payload=random.randint(1000, 10000), qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop

i =0
while i <10:
    print(i)
    time.sleep(1)
    n=random.randint(1000, 10000)
    client.publish("sensor1", payload=n, qos=0)
    i+=1


#client.loop_start()

# i =0
# while i <10:
#     print(i)
#     time.sleep(1)
#     n=random.randint(1000, 10000)
#     client.publish("sensor1", payload=n, qos=0)
#     i+=1

# client.loop_stop()


