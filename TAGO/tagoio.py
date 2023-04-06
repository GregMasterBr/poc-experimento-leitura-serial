
import serial
import serial.tools.list_ports
import paho.mqtt.client as mqtt
import time
import random
from decouple import config, Csv


broker_url = "mqtt.tago.io"
broker_port = 1883
username = "token"  # Substituir pelo seu usuário MQTT do TAGO IO
password = "94624cfa-b7b7-43c8-853a-184b63a6ec42"  # Substituir pela sua senha MQTT do TAGO IO
topic="sensor1"

# Função que lê dados do sensor e publica no broker MQTT
def publish_sensor_data(sensor_port, topic):
    while True:
        try:
            data = random.randint(1000, 10000)
            print(f'{topic}: {data}')
            client.publish(topic, data)
            time.sleep(1)
        except Exception as e:
            print(f'Erro na leitura do sensor {sensor_port}: {e}')
            break

# Conecta ao broker MQTT
client = mqtt.Client(client_id=config("TAGO_IO_NAME_DEVICE"))
client.username_pw_set(username, password)
client.connect(broker_url, broker_port)


client.subscribe(topic)
publish_sensor_data("USBX", topic)

client.loop_forever()
