#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    print("Hi, new client")
    try:
        while True:
            request = await websocket.recv()
            print("A client sent command {}".format(request))
            if request == "GET_TIME":
                response = datetime.datetime.utcnow().isoformat() + 'Z'
            elif request == "GREET_ME":
                response = "Hello, stranger!"
            else:
                response = "ERROR: Command {} not found".format(request)
            await websocket.send(response)
    except websockets.ConnectionClosed:
        print("Bye, client")

start_server = websockets.serve(time, None, 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
