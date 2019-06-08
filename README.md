# WebSockets Python examples

This repo contains a bunch of random WebSockets examples/tests, made for my own learning ~~and amusement~~ and as exploration for another, more complicated project. Thou shalt not use it, unless you like the thrill of hacked-in, not tested, probably unstable code.

## How to use

1. You will need to install [websockets](https://github.com/aaugustin/websockets) first.
1. Clone this repo
1. Choose a test, and open a shell on that directory (you will probably need it)
1. Run the specific instructions for that test

## test1

This example tests WebSockets integration between a Python server and an HTML client. The server can handle multiple clients at once, and each one gets a stream of timestamps, sent at random intervals. The streams are _not_ shared between clients (each client gets its own stream, since a WebSocket, like normal sockets, links one client with one server).

1. Run `python server.py` on the console.
1. Open `client.html` on a web browser. You should see a list of timestamps filling in.
1. You can open `client.html` on multiple tabs at once.
1. Check the server console. It prints "Hello, client" when a new client connects, and "Bye, client" when the client exits. It also prints the timestamps just before sending them. All prints (from all connected clients) get sent to the same output, so they mix together.

## test2

This example tests two-way communications between client and server. The server waits for a message from the client, and then returns something based on the message that the client sent (a simple request-response system).

1. Run `python server.py` on the console.
1. Open `client.html` on a web browser.
1. Type either "GET\_TIME" or "GREET\_ME" on the client's input box. Press the "Send" button.
1. The server console should log the request. The client should display the server response below the input box.

## test3

This example tests cross-device communications. It is almost the same as test2, but it can communicate across a network.

1. Run `python server.py` on the console.
1. Open `client.html` on a web browser _on another device!_.
1. Type the server's IP address on the client's first input box. Press the "Connect" button and hope that it connects...
1. Type either "GET\_TIME" or "GREET\_ME" on the client's second input box. Press the "Send" button.
1. The server console should log the request. The client should display the server response below the input box.

## test4

This example uses two different WebSockets, one for control (client sends commands to server) and one for data (server pushes data to client). This emulates a data acquisition system which allows the user to see the live data and simultaneously control the acquisition.

1. Run `python server.py` on the console.
1. Open `client.html` on a web browser _on another device!_.
1. Type the server's IP address on the client's first input box. Press the "Connect" button and hope that it connects...
1. Type either "STOP" or "START" on the client's second input box to pause and restart the data collection, respectively. Press the "Send" button to submit the command.
1. When you send "START", the text box will start filling with server mock data (from a fake "sensor"). When you send "STOP", the text box will stop filling.
1. The server console should log any commands that it received.

## test4b

This example is functionally identical to test4, but it uses a different architecture for the websockets, which should be cleaner and easier to understand.

1. Follow the instructions for test4.

## test5

This example allows multiple clients to control a single data acquisition server. Some collected data is sent to all clients at once. The server program also logs all received data to a file, but clients only receive a subset of the data.

1. Run `python server.py` on the console.
1. Open `client.html` on two tabs of web browser _on another device!_.
1. On both tabs, type the server's IP address on the client's first input box. Press the "Connect" button and hope that it connects...
1. Type either "STOP" or "START" on the any client's second input box to pause and restart the data collection, respectively. Press the "Send" button to submit the command.
1. When you send "START", both text boxes will start filling with server mock data (from a fake "sensor"). When you send "STOP", both text boxes will stop filling.
1. The server console should log any commands that it received.

## test6

This example adds live data plots on the client side.

1. Follow the instructions for test5.
1. When you start the data acquisition, all client tabs will start updating at the same time. When you stop it, all client tabs will stop too. You can change between tabs and check that they have the same graph.

## test7

This example adds buttons to start and stop data collection, instead of the text box, plus a legend at the bottom of the graph.

1. Follow the instructions for test6.
1. You will not need to type commands. You will find two buttons for starting and stopping the data collection.

## test8

This example adds a sensor which sends multiple data fields at once (maybe a 3-axis accelerometer?). Also, sensors now send a timestamp with their messages.

1. Follow the instructions for test7.

## test9

This example (sorta) hijacks the WebSockets server to also serve the dashboard HTML. You can now simply visit the URL `<the_server_ip>:5678` on the client to get the dashboard.

1. Run `python server.py` on the console.
1. Open a browser on the client, navigate to `<the_server_ip>:5678` or `<the_server_ip>:5678/dashboard`. The browser will show the console.
1. Type the same IP address that you typed above on the input box. Don't include the `:5678/dashboard` part, just the IP. Click on "Connect".
1. Click the Start button to begin displaying data, and the Stop button to pause it.
1. You can open multiple tabs of the dashboard, even on multiple computers. After you connect to the server, they will all update at once, and you can control the server from any one of them.
