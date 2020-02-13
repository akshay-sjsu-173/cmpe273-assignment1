#cmpe273-assignment1

# TCP - Multiple Client Connections

- TCP server starts accepting connections on published port (port #5000 used in the code)
- Client connects with server on published port and waits for acknowledgement ("pong" message)
- Server can handle multiple connections on the same port as each established connection has a
  unique combination of SOURCE_IP, SOURCE_PORT.
- The same client can conenct to the server multiple times as long as it generates a unique SOURCE_PORT
- Client can keep sending messages to the server as long as either the client or server decides to terminate
  the connection. ("Empty message" from client is the terminating condition in above code)

# UDP - Packet Loss Detection

- UDP server starts accepting connections on published port (port #4000 used in the code)
- Client starts sending messages to the servers published port
- Client waits for server acknowledgement before sending next message
- Client resends the message if server does not respond with ACK in X secs. This is packet loss.
- Client performs server reconnect N times before terminating the application.
- If the server starts accepting connections before the Nth retry, client starts sending messages
  from the last pending message id.
