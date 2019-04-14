# -*- coding: utf-8 -*-
"""
@author: Adam Kaliszan
"""

#import IoTShieldAsync as AS
from pymata_aio.pymata_core import PymataCore
from pymata_aio.constants import Constants
import asyncio

board = PymataCore()
board.start()

async def mainLoop():
    await board.set_pin_mode(9, Constants.PWM)
    while True:
        for i in range(80):
            await board.analog_write(9, i)

        for i in range(79, 1, -1):
            await board.analog_write(9, i)
 
        await asyncio.sleep(0.05)

async def main():
    mainTask = asyncio.create_task(mainLoop())
    await mainTask

asyncio.run(main(), debug=True)
