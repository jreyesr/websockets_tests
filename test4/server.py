#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
from time import sleep

recording = False

async def time(websocket, path):
    global recording
    print("Hi, new client")
    try:
        mode = await websocket.recv()
        if mode == "COMMS":
            while True:
                request = await websocket.recv()
                print("A client sent command {}".format(request))
                if request == "START":
                    recording = True
                elif request == "STOP":
                    recording = False
                else:
                    print("ERROR: Command {} not found".format(request))
        elif mode == "DATA":
            while True:
                if recording:
                    await websocket.send(str(int(random.random()*10)))
                await asyncio.sleep(0.1)
    except websockets.ConnectionClosed:
        print("Bye, client")

start_server = websockets.serve(time, None, 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
