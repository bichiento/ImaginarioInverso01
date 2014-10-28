from time import sleep, time
from threading import Thread
from sys import exit
from random import randint
from serial import Serial
from termcolor import colored, cprint
from xml.dom import minidom
from urllib2 import urlopen

SERIAL_PORT_NAME = "/dev/ptyp0"
SERIAL_BAUD_RATE = 57600
SERIAL_WRITE_DELAY = 1.0

MAX_QUEUE_SIZE = 64

def getDataFromXml():
    url = "http://www.xmlfiles.com/examples/cd_catalog.xml"
    xml = minidom.parseString(urlopen(url).read())

    cds = xml.getElementsByTagName('CD')
    cd = cds[randint(0,len(cds)-1)]
    title = cd.getElementsByTagName('TITLE')[0].childNodes[0].nodeValue.decode('utf-8')
    artist = cd.getElementsByTagName('ARTIST')[0].childNodes[0].nodeValue.decode('utf-8')
    return (title, artist)

def setup():
    global mSerial, mQueue, mQueueReadIndex, mQueueWriteIndex, mLastSerialWrite

    mSerial = Serial(SERIAL_PORT_NAME, baudrate=SERIAL_BAUD_RATE, timeout=0.01, writeTimeout=0.5)

    mQueue = []
    mQueueReadIndex = 0
    mQueueWriteIndex = 0
    mLastSerialWrite = time()

def loop():
    global mSerial, mQueue, mQueueReadIndex, mQueueWriteIndex, mLastSerialWrite

    ## write to serial
    if(time()-mLastSerialWrite > SERIAL_WRITE_DELAY):
        mLastSerialWrite = time()

        ## get new piece of xml
        try:
            if(len(mQueue) < MAX_QUEUE_SIZE):
                mQueue.append(getDataFromXml())
            else:
                mQueue[mQueueWriteIndex] = getDataFromXml()
        except Exception as e:
            print "couldn't get XML: "+str(e)
        else:
            mQueueReadIndex = mQueueWriteIndex
            if(len(mQueue) < MAX_QUEUE_SIZE):
                mQueueWriteIndex = len(mQueue)
            else:
                mQueueWriteIndex = (mQueueWriteIndex+1)%len(mQueue)

        ## try to write to serial
        if(len(mQueue) > 0):
            try:
                (txt,author) = mQueue[mQueueReadIndex]
                txt = txt.encode('utf-8')
                author = author.encode('utf-8')
                mSerial.write(txt+"\n")
            except Exception as e:
                print "couldn't write to serial: "+str(e)
            else:
                mQueueReadIndex = (mQueueReadIndex+1)%len(mQueue)

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
    print  "Stoping Serial"
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
