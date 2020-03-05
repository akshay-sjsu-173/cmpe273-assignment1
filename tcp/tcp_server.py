import socket
import time
import _thread as thread


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def new_connection(csock, cid):
    while csock.fileno()>=0:
        data = csock.recv(BUFFER_SIZE)
        if not data:
            print("Closing connection for --> ",cid)
            csock.close()
        else:
            received_data = data.decode().split(',')
            print("Received data : ",received_data[0],":",received_data[3])
            #print(caddr," : ",data.decode())
            csock.send("Server: pong".encode())

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    
    while True:
        c, addr = s.accept()
        #print("Connected to --> ",addr)
        cid = c.recv(BUFFER_SIZE).decode().split(',')[0]
        print("Connected to " + cid)
        thread.start_new_thread(new_connection,(c, cid))
    s.close()

listen_forever()
