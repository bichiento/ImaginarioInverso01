import serial
from time import sleep
port = serial.Serial("/dev/ttyAMA0", 9600, 0.01)
while True:
  data = port.readline()
  sleep(0.1)
  print data
