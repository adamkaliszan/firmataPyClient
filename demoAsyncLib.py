# -*- coding: utf-8 -*-

import IoTShieldAsync as AS

import asyncio

comPort = '/dev/ttyACM0'

myBoard = AS.IoTShield(pwmMax=100)
print("Connection estabilished !!!")

async def mainLoop():
  await myBoard.ioInit()
  while True:
    for i in range(80):
#     await myBoard.leds[1].write(i)
      await myBoard.leds[2].write(i)
#     await myBoard.leds[3].write(i)
#     await myBoard.leds[4].write(i)

    for i in range(79, 1, -1):
#     await myBoard.leds[1].write(i)
      await myBoard.leds[2].write(i)
#     await myBoard.leds[3].write(i)
#     await myBoard.leds[4].write(i)


async def main():
    mainTask = asyncio.create_task(mainLoop())
    await mainTask

asyncio.run(main(), debug=True)
