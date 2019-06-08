#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    print("Hi, client")
    try:
        while True:
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            print(now)
            await websocket.send(now)
            await asyncio.sleep(random.random() * 3)
    except websockets.ConnectionClosed:
        print("Bye, client")

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
