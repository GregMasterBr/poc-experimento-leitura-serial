#!/usr/bin/python

import serial

portCOM = serial.Serial('/dev/ttyUSB0', 115200)
print(portCOM)


while True:
    #data = portCOM.readline(10).decode('utf-8').rstrip()
    data = portCOM.readline().decode('utf-8').rstrip()
    print('data: ', data)
    
