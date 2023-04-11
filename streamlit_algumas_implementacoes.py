import streamlit as st
import paho.mqtt.client as mqtt
from decouple import config, Csv
import random
import time
import pandas as pd
import numpy as np
from PIL import Image

# Inicia a interface do Streamlit
st.title("Leitura de sensores com o protocolo MQTT e 5G")
st.caption('Explicação do projeto. :blue[colors] and emojis :sunglasses:')
st.header('## Sensor de vibração')
chart = st.line_chart((0,0))
#col_sensor1, col_sensor2, col_sensor3 = st.columns(3)
col_sensor1 = st.columns(1)
col1, col2, col3 = st.columns(3)

# Função que é chamada toda vez que o cliente MQTT recebe uma mensagem
def on_message(client, userdata, message):
    # Converte o payload da mensagem para string e atualiza o valor na interface
    data = str(message.payload.decode("utf-8"))
    #st.write(f"{data}")
    topic = message.topic    
    try:
        n= int(data) if data.isnumeric else 0
        chart.add_rows({n})
        st.text("ASdAd: ", data)

    except (RuntimeError, TypeError, NameError, ValueError):
        #st.write(f"Erro")
        pass



#st.metric(label="Temperature", value="70 °F", delta="1.2 °F")    
#st.header("## Sensores")
#col_sensor1, col_sensor2, col_sensor3 = st.columns(3)
# col_sensor1.metric("Potenciomêtro", "70", )
# col_sensor2.metric("Corrente", "9")
#col_sensor3.metric("Vibração", "86%", "4%")

# st.write("### Potenciomêtro")
# st.metric(label="Potenciomêtro", value="70 °F")    
# st.write("### Corrente")
# st.metric("Corrente", "9 mph")
# st.metric(label="Gas price", value=4, delta=-0.5,
#     delta_color="inverse")

# st.metric(label="Active developers", value=123, delta=123,
#     delta_color="off")


img_file_buffer = st.camera_input("Capturar uma foto")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
    st.code(bytes_data, language="text")

    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    #st.write(img_array.shape)    
    st.image(img, caption='Sunrise by the mountains')


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

