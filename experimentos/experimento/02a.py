import serial
import paho.mqtt.client as mqtt
import random
from decouple import config, Csv


# Configurações do MQTT
mqtt_broker = config("HIVEMQ_CLUSTER_URL")
mqtt_port = 8883

# Conexões com o MQTT
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(config("HIVEMQ_USERNAME"), config("HIVEMQ_PASSWORD"))

mqtt_client.connect(mqtt_broker, mqtt_port)

sensor1_topic = 'sensores/sensor1'

sensor2_topic = 'sensores/sensor2'


while True:
    print("While")
    # Ler dados do sensor 1
    #sensor1_data = ser1.readline().decode().strip()
    sensor1_data = random.randint(1000, 10000)

    # Enviar dados do sensor 1 para o MQTT
    mqtt_client.publish(sensor1_topic, sensor1_data)

    # Ler dados do sensor 2
    #sensor2_data = ser2.readline().decode().strip()
    sensor2_data = random.randint(1000, 10000)

    # Enviar dados do sensor 2 para o MQTT
    mqtt_client.publish(sensor2_topic, sensor2_data)
