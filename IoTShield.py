# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:29:04 2018

@author: Adam Kaliszan
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

class Key:
    def __init__(self, board, pinNo):
        self.__board = board        
        self.__pinNo = pinNo
        board.set_pin_mode(pinNo, Constants.INPUT)
        board.digital_write(pinNo, 1)                
        
    def read(self):
        return True if self.__board.digital_read(self.__pinNo) == 0 else False

class Led:
    def __init__(self, board, pinNo, reverse=False, mode=Constants.OUTPUT, maxValue=100 ):      
        self.__board = board        
        self.__pinNo = pinNo
        self.__mode = Constants.PWM if mode == Constants.PWM else Constants.OUTPUT
        self.__maxValue = maxValue if self.__mode == Constants.PWM else 1
        self.__state = 0
        self.__convertValue = (lambda x:self.__maxValue - x) if reverse==True else (lambda x:x)

        self.__write = board.analog_write if mode == Constants.PWM else board.digital_write        

        self.__board.set_pin_mode(pinNo, mode)
        self.off()
        
    def state(self):
        return self.__state        
        
    def write(self, value):
        self.__state = value
        if self.__state > self.__maxValue: self.__state=self.__maxValue
        if self.__state < 0: self.__state = 0
        self.__write(self.__pinNo, self.__convertValue(self.__state))
            
    def on(self):
        self.__state=self.__maxValue
        self.__write(self.__pinNo, self.__convertValue(self.__state))
        
    def off(self):
        self.__state=0
        self.__write(self.__pinNo, self.__convertValue(self.__state))
        
    def toggle(self):
        self.__state = self.__maxValue - self.__state        
        self.__write(self.__pinNo, self.__convertValue(self.__state))
    
class AnalogSensor:
    def __init__(self, board, pinNo):
        self.__board=board
        self.__pinNo=pinNo        
        board.set_pin_mode(pinNo, Constants.ANALOG)

    def read(self):
        return self.__board.analog_read(self.__pinNo)

class IoTShield:
    def __init__(self, port='', pwmMax=100):
        board = None        
        
        try:
            #Board init
            if len(port) > 0:
                board = PyMata3(com_port=port)
            else:
                board = PyMata3()
                                
                                
            print("Firmware version {0}".format(board.get_firmware_version()))
        except Exception as excObj:
            print("Something is wrong: {0}".format(excObj))
            raise excObj

        self.__board = board
        #Led init
        self.leds = {
            1: Led(board, 10, False, Constants.PWM,    pwmMax),
            2: Led(board,  9, False, Constants.PWM,    pwmMax),
            3: Led(board,  5, False, Constants.PWM,    pwmMax),
            4: Led(board,  4, False, Constants.OUTPUT, 1),
            5: Led(board,  8, True,  Constants.OUTPUT, 1)        
        }
        #Buzzer init

        #Keyboard init
        self.keys = {
            1: Key(board, 13),
            2: Key(board, 12),
            3: Key(board, 7),
            4: Key(board, 8)
        }
        #Sensors init
        self.SensorLight       = AnalogSensor(board, 0)        
        self.SensorTemperature = AnalogSensor(board, 1)
        self.SensorAlcohol     = AnalogSensor(board, 2)
        self.SensorAxisX       = AnalogSensor(board, 3)
        self.SensorAxisY       = AnalogSensor(board, 4)
        self.SensorAxisZ       = AnalogSensor(board, 5)
        
    def sleep(self, time):
        self.__board.sleep(time)
        
