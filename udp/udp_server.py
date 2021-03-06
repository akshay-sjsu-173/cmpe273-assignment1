import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
#MESSAGE = "Server : pong"

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))

    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        print(ip, " : ", data.decode(encoding="utf-8").strip())
        # reply back to the client
        MESSAGE = "Ack --> "+data.decode(encoding="utf-8").strip()
        s.sendto(MESSAGE.encode(), ip)

listen_forever()
