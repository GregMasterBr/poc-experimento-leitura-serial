import serial.tools.list_ports

usb_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'USB' in p.interface
]

print('Portas USB disponíveis:')
for port in usb_ports:
    print(port)
