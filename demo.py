# -*- coding: utf-8 -*-

import IoTShield


comPort = '/dev/ttyACM0'

myBoard = IoTShield.IoTShield2(pwmMax=100)
print("Connection estabilished !!!")

ledNo=1
while True:
#    try:
    myBoard.leds[ledNo].toggle()    
    myBoard.sleep(1)

    myBoard.leds[ledNo].toggle()
    myBoard.sleep(1)
        
    ledNo = 1 if ledNo == 5 else ledNo+1
    
    value = myBoard.SensorTemperature.read()    
    print("Temperature: {0}".format(value))
    
    value = myBoard.SensorLight.read()    
    print("Light: {0}".format(value))
    


if myBoard: myBoard.Shutdown()