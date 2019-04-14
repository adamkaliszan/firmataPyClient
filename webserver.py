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

import IoTShieldAsync as AS

app = web.Application()

myBoard = AS.IoTShield(pwmMax=100)
print("Connection estabilished !!!")

async def ledCr():
    await myBoard.ioInit()
    while True:
        for i in range(80):
            await myBoard.leds[2].write(i)
            await myBoard.sleep(0.1)

        for i in range(79, 1, -1):
            await myBoard.leds[2].write(i)
            await myBoard.sleep(0.1)

async def start_background_tasks(app):
    app['ledCr'] = app.loop.create_task(ledCr())


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)



app.router.add_static('/html', path='./html/')
app.add_routes([
                web.get('/', handle),
                web.get('/{name}', handle)])

app.on_startup.append(start_background_tasks)


web.run_app(app)
