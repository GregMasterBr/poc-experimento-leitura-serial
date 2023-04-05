import serial.tools.list_ports

usb_ports = serial.tools.list_ports.comports()

print('Portas USB disponíveis:')
print(usb_ports)
for port in usb_ports:
    if 'USB' in port.interface:
        print(f'{port.device} - {port.description}', end='')
        try:
            ser = serial.Serial(port.device)
            ser.close()
            print(' (Não utilizada)')
        except serial.SerialException:
            print(' (Utilizada)')
