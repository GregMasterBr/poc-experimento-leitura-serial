import time
import paho.mqtt.client as paho
from paho import mqtt
from decouple import config, Csv
import random
import serial


# Create serial objects for each sensor
sensor1 = serial.Serial(config("SENSOR_1"), config("SENSOR_1_BAUD")) #potenciometro
sensor2 = serial.Serial(config("SENSOR_2"), config("SENSOR_2_BAUD")) #sensor corrente
#sensor3 = serial.Serial(config("SENSOR_3"), config("SENSOR_3_BAUD"))

print("Sensor 1: ",sensor1)
print("Sensor 2: ",sensor2)
#print("Sensor 3: ",sensor3)


# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid) + " USERDATA: " + str(userdata))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

client = paho.Client(client_id="HIVEMQ", userdata=None, protocol=paho.MQTTv5)

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set(config("HIVEMQ_USERNAME"), config("HIVEMQ_PASSWORD"))

# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(config("HIVEMQ_CLUSTER_URL"), config("HIVEMQ_PORT", cast=int))

# setting callbacks, use separate functions like above for better visibility
#topics = [("sensor1", 1), ("sensor2", 2), ("sensor3", 0)]
topics = [("sensor1", 0), ("sensor2", 0), ("sensor3", 0)]

#client.subscribe(topics)
#client.on_message = on_message
client.on_publish = on_publish

while True:
    
    #timestamp = time.time()

    #print("oi")
    # Read data from sensor 1
    #if sensor1.in_waiting > 0:
    data1 = sensor1.readline().decode('utf-8').rstrip()
    #print(timestamp,"-->Sensor 1:", data1)
    client.publish('sensor1', payload = data1 , qos = 0)
    
    
    time.sleep(4/1000);
    
    # Read data from sensor 2
    #if sensor2.in_waiting > 0:
    data2 = sensor2.readline().decode('utf-8').rstrip()
    #print(timestamp,"-->Sensor 2:", data2)
    client.publish('sensor2', payload = data2 , qos = 0)
    
    time.sleep(1.5/1000);
    
    # Read data from sensor 3
    #if sensor3.in_waiting > 0:
    #data3 = sensor3.readline().decode('utf-8').rstrip()
    data3 = '4';
    client.publish('sensor3', payload = data3 , qos = 0)
    #print(timestamp,"--> Sensor 3:", data3)
    time.sleep(1.5/1000);
    
    sensor1.flushInput()
    sensor2.flushInput()
    #sensor3.flushInput()
