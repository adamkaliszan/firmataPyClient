# -*- coding: utf-8 -*-

import IoTShield as AS


comPort = '/dev/ttyACM0'

myBoard = AS.IoTShield(pwmMax=100)
print("Connection estabilished !!!")

ledNo=1
while True:
    myBoard.sleep(1)
        
    ledNo = 1 if ledNo == 5 else ledNo+1
    
    if myBoard.keys[1].read():
        myBoard.leds[ledNo].write(20)
    else:
        myBoard.leds[ledNo].off()
        
    
    value = myBoard.SensorTemperature.read()    
    print("Temperature: {0}".format(value))
    
    value = myBoard.SensorLight.read()    
    print("Light: {0}".format(value))
    
