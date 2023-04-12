import serial
import paho.mqtt.client as mqtt

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

# Inicialização das portas seriais
ser1 = serial.Serial(sensor1_port, sensor1_baud)
ser2 = serial.Serial(sensor2_port, sensor2_baud)

# Loop infinito para ler os dados dos sensores e publicá-los no MQTT
while True:
    # Ler dados do sensor 1 e publicar no MQTT
    if ser1.in_waiting > 0:
        sensor1_data = ser1.readline().decode().strip()
        mqtt_client.publish(sensor1_topic, sensor1_data)
    
    # Ler dados do sensor 2 e publicar no MQTT
    if ser2.in_waiting > 0:
        sensor2_data = ser2.readline().decode().strip()
        mqtt_client.publish(sensor2_topic, sensor2_data)
