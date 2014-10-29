import serial
from time import sleep
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.01)
while True:
  data = port.readline()
  sleep(0.1)
  print data
