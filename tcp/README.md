# TCP - Multiple Client Connections

- TCP server starts accepting connections on published port (port #5000 used in the code)
- Client connects with server on published port and waits for acknowledgement ("pong" message)
- Server can handle multiple connections on the same port as each established connection has a
  unique combination of SOURCE_IP, SOURCE_PORT. 
- The same client can conenct to the server multiple times as long as it generates a unique SOURCE_PORT
