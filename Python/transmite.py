import serial
from time import sleep
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.01, writeTimeout=0.5))
while (True):
  port.write("HOLA ASTROS\n")
  sleep(1.0)
port.close()
