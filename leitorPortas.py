import serial
import time

# Define the serial ports for each sensor
sensor1_port = '/dev/ttyUSB0'
sensor2_port = '/dev/ttyUSB1'
#sensor3_port = '/dev/ttyUSB2'

# Define the baud rate for each sensor
sensor1_baud = 115200
sensor2_baud = 9600
#sensor3_baud = 115200

# Create serial objects for each sensor
sensor1 = serial.Serial(sensor1_port, sensor1_baud)
sensor2 = serial.Serial(sensor2_port, sensor2_baud)
#sensor3 = serial.Serial(sensor3_port, sensor3_baud)

print('------------------------ Portas COM ------------------------')
print('Portas sensor1:',sensor1)
print('Portas sensor2:',sensor2)
#print('Portas sensor3:',sensor3)

while True:
    timestamp = time.time()
    # Read data from sensor 1
    if sensor1.in_waiting > 0:
        data1 = sensor1.readline().decode('utf-8').rstrip()
        print(timestamp,"-->Sensor 1:", data1)

    # Read data from sensor 2
    if sensor2.in_waiting > 0:
        data2 = sensor2.readline().decode('utf-8').rstrip()
        print(timestamp,"-->Sensor 2:", data2)

    # Read data from sensor 3
    #if sensor3.in_waiting > 0:
        #data3 = sensor3.readline().decode('utf-8').rstrip()
        #print(timestamp,"--> Sensor 3:", data3)