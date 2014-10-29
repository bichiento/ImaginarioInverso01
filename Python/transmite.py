import serial
port = serial.Serial(/dev/ttyAMA0, 9600, 0.01)
port.write("HOLA ASTROS")
port.close()