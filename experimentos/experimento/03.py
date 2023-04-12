import serial
import paho.mqtt.client as mqtt
import threading

# Configurações do MQTT
mqtt_broker = 'mqtt.example.com'
mqtt_port = 1883

# Configurações do sensor 1
sensor1_port = '/dev/ttyUSB0'
sensor1_baud = 9600
sensor1_topic = 'sensores/sensor1'

# Configurações do sensor 2
sensor2_port = '/dev/ttyUSB1'
sensor2_baud = 9600
sensor2_topic = 'sensores/sensor2'

# Conexões com o MQTT
mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)

# Função para ler e publicar dados do sensor 1
def read_sensor1():
    ser1 = serial.Serial(sensor1_port, sensor1_baud)
    while True:
        sensor1_data = ser1.readline().decode().strip()
        mqtt_client.publish(sensor1_topic, sensor1_data)

# Função para ler e publicar dados do sensor 2
def read_sensor2():
    ser2 = serial.Serial(sensor2_port, sensor2_baud)
    while True:
        sensor2_data = ser2.readline().decode().strip()
        mqtt_client.publish(sensor2_topic, sensor2_data)

# Criar threads para ler e publicar dados dos sensores
thread1 = threading.Thread(target=read_sensor1)
thread2 = threading.Thread(target=read_sensor2)

# Iniciar as threads
thread1.start()
thread2.start()
