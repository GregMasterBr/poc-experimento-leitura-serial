import streamlit as st
import paho.mqtt.client as mqtt
from decouple import config, Csv
import random
import time
 
# Função que é chamada toda vez que o cliente MQTT recebe uma mensagem
def on_message(client, userdata, message):
    # Converte o payload da mensagem para string e atualiza o valor na interface
    data = str(message.payload.decode("utf-8"))
    topic = message.topic
    st.write(f"{topic}: {data}")

# Cria o cliente MQTT e o conecta ao broker
client = mqtt.Client()
client.username_pw_set(config("HIVEMQ_USERNAME"), config("HIVEMQ_PASSWORD"))
client.tls_set()
client.connect(config("HIVEMQ_CLUSTER_URL"), config("HIVEMQ_PORT", cast=int))

# Inscreve o cliente MQTT nos tópicos desejados
topics = [("sensor1", 0), ("sensor2", 0), ("sensor3", 0)]
client.subscribe(topics)

# Configura a função on_message para ser chamada toda vez que o cliente MQTT receber uma mensagem
client.on_message = on_message

# Inicia a interface do Streamlit
st.title("Dashboard MQTT 2")

# Mantém a conexão com o broker MQTT e atualiza a interface em tempo real
i=0
while True:
    #client.loop()
    time.sleep(5)
    n=random.randint(1000, 10000)
    i+=1
    st.write(f"{i}:  {n}")

