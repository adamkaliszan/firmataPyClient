# -*- coding: utf-8 -*-

import IoTShield as AS
import socket


myBoard = AS.IoTShield(pwmMax=100)
print("Connection with Arduino estabilished !!!")

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 50  # Normally 1024, but we want fast response


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:    
    conn, addr = s.accept()
    print ("Connection with client was established")
    
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
    
        if data == "led1on":
            myBoard.leds[1].on()

        if data == "led1off":
            myBoard.leds[1].off()
            
    conn.close()
