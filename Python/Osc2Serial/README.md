Simple server that turns Osc messages into Serial messages

-- Dependencies  
- pySerial  
    wget https://pypi.python.org/packages/source/p/pyserial/pyserial-2.6.tar.gz -O - | tar -xz  
    cd pyserial-2.6
    sudo python setup.py install
- liblo:  
    sudo apt-get install liblo-dev  
- pyliblo:  
    wget http://das.nasophon.de/download/pyliblo-0.9.2.tar.gz -O - | tar -xz  
    cd pyliblo-0.9.2  
    sudo ./setup.py build  
    sudo ./setup.py install  
