#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue April  14 10:36:29 2019

@author: Adam Kaliszan
"""

import requests
import json
import time

import asyncio
from aiohttp import web

import IoTShieldAsync as AS

app = web.Application()

myBoard = AS.IoTShield(pwmMax=100)
print("Connection estabilished !!!")

async def ledCr():
  await myBoard.ioInit()
  while True:
    await myBoard.sleep(10)
    continue
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


async def ledPutHandle(request):
  ledNumber = int(request.match_info.get('number', "0"))
  ledValue = -1
  if request.body_exists and ledNumber > 0:
#   print(await request.read())
    data = await request.json()
    ledValue = int(data["value"])

  if ledValue >= 0 and ledNumber >= 1 and ledNumber <= 5: 
    await myBoard.leds[ledNumber].write(ledValue)

  return web.Response(text=f"Led {ledNumber} value changed into {ledValue}")

app.router.add_static('/html', path='./html/')
app.add_routes(
  [
    web.get('/', handle)
  , web.put('/led/{number}', ledPutHandle)
  , web.get('/{name}', handle)
  ])

app.on_startup.append(start_background_tasks)


web.run_app(app)
