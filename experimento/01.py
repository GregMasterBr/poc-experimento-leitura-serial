import serial
import paho.mqtt.client as mqtt

# Configurações do serial
serial_port = '/dev/ttyUSB0'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)

# Configurações do MQTT
mqtt_broker = 'mqtt.example.com'
mqtt_port = 1883
mqtt_topic = 'sensores'

# Conexão com o MQTT
mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)

while True:
    # Ler dados do sensor
    sensor_data = ser.readline().decode().strip()

    # Enviar dados para o MQTT
    mqtt_client.publish(mqtt_topic, sensor_data)
