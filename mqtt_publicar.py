import paho.mqtt.client as mqtt
from decouple import config, Csv
# setting callbacks for different events to see if it works, print the message etc.

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

cliente=mqtt.Client(client_id="", protocol=mqtt.MQTTv5)

cliente.on_connect = on_connect

# enable TLS for secure connection
cliente.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

#coxexao = cliente.connect(host="broker.mqttdashboard.com")
cliente.username_pw_set(config("HIVEMQ_USERNAME"), config("HIVEMQ_PASSWORD"))

coxexao = cliente.connect(host="413fa6911e6340d5b278f78d5d12f336.s2.eu.hivemq.cloud", port=8883)

cliente.publish(topic="sensor1", payload="369")

print("fim")