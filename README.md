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
