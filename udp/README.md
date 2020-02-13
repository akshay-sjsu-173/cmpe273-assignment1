# UDP - Packet Loss Detection

- UDP server starts accepting connections on published port (port #4000 used in the code)
- Client starts sending messages to the servers published port
- Client waits for server acknowledgement before sending next message
- Client resends the message if server does not respond with ACK in X secs. This is packet loss.
- Client performs server reconnect N times before terminating the application.
- If the server starts accepting connections before the Nth retry, client starts sending messages
  from the last pending message id. 
