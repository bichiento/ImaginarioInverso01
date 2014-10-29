import serial
from time import sleep
port = serial.Serial("/dev/ttyAMA0", 9600, 0.01)
while (True):
  port.write("HOLA ASTROS\n")
  sleep(1.0)
port.close()
