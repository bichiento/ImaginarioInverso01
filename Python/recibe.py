import serial
from time import sleep
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.01)
while True:
  data = port.readline()
  if data:
    print data    
  sleep(0.1)
