import random
import time
import ssl
import paho.mqtt.client as mqtt

broker_url = "mqtt.tago.io"
broker_port = 8883
username = "Token"  # Substituir pelo seu usuário MQTT do TAGO IO
password = "94624cfa-b7b7-43c8-853a-184b63a6ec42"  # Substituir pela sua senha MQTT do TAGO IO
from decouple import config, Csv
# Cria o cliente MQTT e inicia o loop de leitura de mensagens
client = mqtt.Client(client_id=config("TAGO_IO_NAME_DEVICE"))
client.username_pw_set(username, password)
client.tls_set_context(ssl.create_default_context())
client.connect(broker_url, broker_port)

topics = [("sensor1", 0), ("sensor2", 0), ("sensor3", 0)]

client.subscribe("sensor1",qos=1)
client.publish("sensor1", payload=random.randint(100, 1000), qos=1)

#client.loop_forever()

