# -*- coding: utf-8 -*-

import asyncio
from bleak import discover

async def run():
    devices = await discover()
    for d in devices:
        print(d)#d.address,d.name,d.rssi

loop = asyncio.get_event_loop()
loop.run_until_complete(run())