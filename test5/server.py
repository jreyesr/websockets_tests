#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
from time import sleep
import _thread
import queue

recording = False
DATA_STREAMS = []
main_queue = queue.Queue()

def send_entry(message, queues):
    for q in queues:
        q.put(message)

def read_sensor():
    i = 0
    while True:
        if recording:
            message = "SENSOR,{}\n".format(int(random.random()*10))
            main_queue.put(message)
            
            # only stream one message in each 4 (AKA once per second)
            i = (i + 1) % 4
            if i == 0:
                send_entry(message, DATA_STREAMS)
        sleep(.25)
    
def log_data():
    FILENAME = "log.txt"
    with open(FILENAME, "w+") as full: # log data to file
        while True:
            new_msg = main_queue.get()
            full.write(new_msg)
            full.flush() # HACK: file does not save the data otherwise (?)
            
_thread.start_new_thread(read_sensor, ())
_thread.start_new_thread(log_data, ())

async def serve(websocket, path):
    import queue
    global recording
    my_queue = queue.Queue()
    try:
        if path == "/commands/":
            print("Hi, new client")
            while True:
                request = await websocket.recv()
                print("A client sent command {}".format(request))
                if request == "START":
                    recording = True
                elif request == "STOP":
                    recording = False
                else:
                    print("ERROR: Command {} not found".format(request))
        elif path == "/stream_data/":
            DATA_STREAMS.append(my_queue)
            while True:
                try:
                    await websocket.send(my_queue.get(block=False))
                except queue.Empty:
                    pass
                await asyncio.sleep(0.1)
    except websockets.ConnectionClosed:
        print("Bye, client")
        if my_queue in DATA_STREAMS:
            DATA_STREAMS.remove(my_queue)

start_server = websockets.serve(serve, None, 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

