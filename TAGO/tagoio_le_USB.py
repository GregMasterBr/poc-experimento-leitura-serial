
import serial
import serial.tools.list_ports
import paho.mqtt.client as mqtt
import time

broker_url = "mqtt.tago.io"
broker_port = 1883
username = "token"  # Substituir pelo seu usuário MQTT do TAGO IO
password = "94624cfa-b7b7-43c8-853a-184b63a6ec42"  # Substituir pela sua senha MQTT do TAGO IO

# Função que lê dados do sensor e publica no broker MQTT
def publish_sensor_data(sensor_port, topic):
    ser = serial.Serial(sensor_port, 9600)
    while True:
        try:
            data = ser.readline().decode('ascii').strip()
            print(f'{topic}: {data}')
            client.publish(topic, data)
            time.sleep(1)
        except Exception as e:
            print(f'Erro na leitura do sensor {sensor_port}: {e}')
            break
    ser.close()

# Conecta ao broker MQTT
client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(broker_url, broker_port)

# Lista as portas USB disponíveis e inicia a leitura dos sensores
usb_ports = serial.tools.list_ports.comports()

print('Portas USB disponíveis:')
for port in usb_ports:
    if 'USB' in port.interface:
        print(f'{port.device} - {port.description}')
        topic = f'tago/data/{port.description}'
        client.subscribe(topic)
        publish_sensor_data(port.device, topic)

client.loop_forever()
