import streamlit as st
import paho.mqtt.client as mqtt
from decouple import config, Csv
import math

# Inicia a interface do Streamlit
st.title("Leitura de sensores com o protocolo MQTT e 5G")
st.caption('Projeto para demonstrar viabilidade do uso 5G para projetos IOTs')

c1 = st.container()
with c1:
    st.header('## Potenciômetro')
    potenciometro = st.progress(0, text="0")


c2 = st.container()
with c2:
    st.header('## Sensores')


placeholder = st.empty()


c3 = st.container()
with c3:
    st.header('## Chart ')
    vibracao = st.line_chart((0,0))


# Função que é chamada toda vez que o cliente MQTT recebe uma mensagem
def on_message(client, userdata, message):
    # Converte o payload da mensagem para string e atualiza o valor na interface
    data = str(message.payload.decode("utf-8"))
    topic = message.topic     
    try:
        if topic=="sensor1":
            n = int(data) if data.isnumeric else 0
            with c1:
                potenciometro.progress(math.floor(n/40.95), text=f"{n}")            
        elif topic=="sensor2":
            n = float(data) if data.isnumeric else 0.0            
            with placeholder.container():  
                col1, col2 = st.columns(2)          
                col1.metric(label="Sensor de corrente", value=n)
        elif topic=="sensor3":
            n = float(data) if data.isnumeric else 0.0            
            with placeholder.container():  
                col1, col2 = st.columns(2)          
                col2.metric(label="Sensor de vibração", value=n)                
        else:
            pass            
    except (RuntimeError, TypeError, NameError, ValueError):
        #st.write(f"Erro")        
        pass


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

# Mantém a conexão com o broker MQTT e atualiza a interface em tempo real
while True:
    try:
        client.loop()
    except (RuntimeError, TypeError, NameError):
        pass

