import streamlit as st
import paho.mqtt.client as mqtt
from decouple import config, Csv
import random
import time
import pandas as pd
import numpy as np
from PIL import Image
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
    print(f'{topic}: {data}')
    try:
        if topic=="sensor1":
            n = int(data) if data.isnumeric else 0
            with c1:
                potenciometro.progress(math.floor(n/40.95), text=f"{n}")            
        elif topic=="sensor2":
            n = float(data) if data.isnumeric else 0.0
            print(topic, n)
            with placeholder.container():  
                col1, col2 = st.columns(2)          
                col1.metric(label="Sensor de corrente", value=n)
                col2.metric(label="Sensor de vibração", value=None)            
        elif topic=="sensor3":
            n= int(data) if data.isnumeric else 0
            vibracao.add_rows({n})
            
        else:
            pass            
    except (RuntimeError, TypeError, NameError, ValueError):
        #st.write(f"Erro")
        pass

# img_file_buffer = st.camera_input("Capturar uma foto")

# if img_file_buffer is not None:
#     # To read image file buffer as bytes:
#     bytes_data = img_file_buffer.getvalue()
#     # Check the type of bytes_data:
#     # Should output: <class 'bytes'>
#     st.write(type(bytes_data))
#     st.code(bytes_data, language="text")

#     # To read image file buffer as a PIL Image:
#     img = Image.open(img_file_buffer)

#     # To convert PIL Image to numpy array:
#     img_array = np.array(img)

#     # Check the type of img_array:
#     # Should output: <class 'numpy.ndarray'>
#     st.write(type(img_array))

#     # Check the shape of img_array:
#     # Should output shape: (height, width, channels)
#     #st.write(img_array.shape)    
#     st.image(img, caption='Sunrise by the mountains')



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

