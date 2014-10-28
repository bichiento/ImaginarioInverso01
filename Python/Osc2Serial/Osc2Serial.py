from time import sleep, time
from threading import Thread
from sys import exit
from Queue import Queue
from serial import Serial
from OSC import OSCServer
from termcolor import colored, cprint


SERIAL_PORT_NAME = "/dev/ptyp1"
SERIAL_BAUD_RATE = 57600
SERIAL_WRITE_DELAY = 1.0

OSC_IN_ADDRESS = "127.0.0.1"
OSC_IN_PORT = 8888
OSC_MESSAGE_PATH = "/imaginario/html"

def _oscHandler(addr, tags, stuff, source):
    if (addr == OSC_MESSAGE_PATH):
        msg = stuff[0].decode('utf-8')
        print "%s : %s"%(addr, msg)
        mQueue.put(msg)
    else:
        print "%s"%(addr)

def setup():
    global mServer, mQueue, mLastSerialWrite, mSerial, oscThread

    mQueue = Queue()
    mLastSerialWrite = time()
    mSerial = Serial(SERIAL_PORT_NAME, baudrate=SERIAL_BAUD_RATE, timeout=0.01)

    mServer = OSCServer((OSC_IN_ADDRESS, OSC_IN_PORT))
    mServer.addMsgHandler('default', _oscHandler)
    oscThread = Thread(target = mServer.serve_forever)
    oscThread.start()
    print "OSCServer ready"

def loop():
    global mLastSerialWrite, mQueue

    ## write serial
    if((time()-mLastSerialWrite > SERIAL_WRITE_DELAY) and (not mQueue.empty())):
        mLastSerialWrite = time()
        txt = mQueue.get().encode('utf-8')
        mSerial.write(txt+"\n")

    ## read serial
    msg = ""
    for line in mSerial:
        msg += line
    if msg:
        cprint("CO", 'white', 'on_green', attrs=['bold'], end='')
        cprint("DE", 'grey', attrs=['bold'], end='')
        cprint("PI", 'white', 'on_red',   attrs=['bold'], end='    ')
        cprint(" * * * ASTROVANDALISTAS * * * ", attrs=['bold', 'reverse'], end='    ')
        cprint("CO", 'white', 'on_green', attrs=['bold'], end='')
        cprint("DE", 'grey', attrs=['bold'], end='')
        cprint("PI", 'white', 'on_red',   attrs=['bold'], end='\n')
        cprint("OUTPUT", attrs=['bold', 'blink'], end=': ')
        cprint(msg, end='\n')

def cleanUp():
    print  "Stoping OSCServer"
    mServer.close()
    oscThread.join()
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
