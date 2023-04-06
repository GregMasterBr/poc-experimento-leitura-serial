import paho.mqtt.client as mqtt
from decouple import config, Csv
import time

def receber_mensagem(client, userdata, message):
    time.sleep(1)
    print("Mensagem recebida: " )
    print(str(message.payload.decode("utf-8")))

cliente=mqtt.Client(client_id="rasp", protocol=mqtt.MQTTv5)
#coxexao = cliente.connect(host="broker.mqttdashboard.com")
coxexao = cliente.connect(host=config("HIVEMQ_CLUSTER_URL"), port=config("HIVEMQ_PORT", cast=int))

cliente.loop_start()
cliente.subscribe("sensor1")


while True:
    cliente.on_message=receber_mensagem