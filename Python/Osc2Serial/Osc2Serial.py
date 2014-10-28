from time import sleep, time
from sys import exit
from Queue import Queue
from serial import Serial
from liblo import *


SERIAL_PORT_NAME = "/dev/ptyp1"
SERIAL_BAUD_RATE = 57600
SERIAL_WRITE_DELAY = 5.0

OSC_MESSAGE_PATH = "/imaginario/html"


class OscServer(ServerThread):
    def __init__(self):
        ServerThread.__init__(self, 8888)

    @make_method(OSC_MESSAGE_PATH, 's')
    def look_callback(self, path, args):
        print "%s : %s"%(path, args)
        mQueue.put(args[0])

    @make_method(None, None)
    def default_callback(self, path, args):
        print "%s"%path

def setup():
    global mServer, mQueue, mLastLook, mSerial

    mQueue = Queue()
    mLastLook = time()
    mSerial = Serial(SERIAL_PORT_NAME, baudrate=SERIAL_BAUD_RATE, timeout=0.01)

    try:
        mServer = OscServer()
        mServer.start()
    except ServerError as e:
        print str(e)
        exit(0)

def loop():
    global mLastLook
    if((time()-mLastLook > WRITE_SERIAL_DELAY) and not mQueue.empty()):
        mLastLook = time()
        txt = mQueue.get()
        mSerial.write(txt)

def cleanUp():
    print  "Stoping OSCServer"
    mServer.stop()
    mSerial.close()

if __name__=="__main__":
    setup()

    while True:
        try:
            loopStart = time()
            loop()
            loopTime = time() - loopStart
            sleep(max(0.016 - loopTime, 0))
        except KeyboardInterrupt:
            cleanUp()
            exit(0)
        except Exception as e:
            print "loop caught: "+str(e)
            cleanUp()
            setup()
