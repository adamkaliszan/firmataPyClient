# -*- coding: utf-8 -*-

import IoTShield as AS
import socket


myBoard = AS.IoTShield(pwmMax=100)
print("Connection with Arduino estabilished !!!")

TCP_IP = '0.0.0.0'
TCP_PORT = 5001
BUFFER_SIZE = 50  # Normally 1024, but we want fast response


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:    
    print ("Waiting for new connection")
    conn, addr = s.accept()
    print ("Connection with client was established")
    
    while True:
        data = conn.recv(BUFFER_SIZE).decode()
        if not data: break
    
        data = data.rstrip()    
    
        if data == "ping":
            conn.send("pong".encode())
    
        if data == "led2on":
            myBoard.leds[2].on()

        if data == "led2off":
            myBoard.leds[2].off()
            
        print("Received " + data)
            
    conn.close()
