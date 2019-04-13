#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue April  14 10:36:29 2019

@author: Adam Kaliszan
"""
import asyncio
import requests
import json
import time
from aiohttp import web
import IoTShield as AS


comPort = '/dev/ttyACM0'
myBoard = AS.IoTShield(pwmMax=100)
print("Connection estabilished !!!")

myBoard.leds[1].write(20)
myBoard.leds[2].write(20)
myBoard.leds[3].write(20)
myBoard.leds[4].write(20)
myBoard.sleep(3)


#async def ledCr():
#    while True:
#        for i in range(100):
#            await myBoard.leds[1].write(i)
#            myBoard.leds[2].write(i)
#            await myBoard.leds[3].write(i)
#            await myBoard.leds[4].write(i)
#        await asyncio.sleep(1)


async def start_background_tasks(app):
    app['ledCr'] = app.loop.create_task(ledCr())


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.router.add_static('/html', path='./html/')
app.add_routes([
                web.get('/', handle),
                web.get('/{name}', handle)])

#app.on_startup.append(start_background_tasks)


web.run_app(app)
