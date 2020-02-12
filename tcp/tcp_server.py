import socket
import time
import _thread as thread


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def new_connection(csock, caddr):
    while csock.fileno()>=0:
        data = csock.recv(BUFFER_SIZE)
        if not data:
            print("Closing connection for --> ",caddr)
            csock.close()
        else:
            print(caddr," : ",data.decode())
            csock.send("Server: pong".encode())

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    
    while True:
        c, addr = s.accept()
        print("Connected to --> ",addr)
        thread.start_new_thread(new_connection,(c, addr))
    s.close()

listen_forever()
