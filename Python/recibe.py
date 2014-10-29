import serial
port = serial.Serial(/dev/ttyAMA0, 9600, 0.01)
data = port.read(numberofbytes)
print data