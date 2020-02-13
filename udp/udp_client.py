'''
This script requires the module func_timeout.

Run the following command to install func_timeout :-
  
  pip3 install func_timeout -t /usr/lib/python3.8/

'''

import socket
from func_timeout import func_timeout

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024

def getNewConnection():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendMessage(s=None):
    wait_time = 3
    try:
        if not s:
            s = getNewConnection() #socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_ack = True
        with open('upload.txt','r') as currFile:
            message = currFile.readline() #Read first line in file 
            message_state = [message,5] #(message, re-connect count)
            while message:
                if message != message_state[0]:
                    message_state = [message,5] #Reset re-connect count for a new message
                print("You : ",message.strip())
                s.sendto(str(message).encode(), (UDP_IP, UDP_PORT))
                try:
                    data, ip = func_timeout(wait_time,s.recvfrom,(BUFFER_SIZE,))
                    print(data.decode().strip())
                    message = currFile.readline() #Read next line if server ack received
                except:
                    print("Server did not respond in ",wait_time," secs. Resending package --> ", message_state)
                    message_state[1] -= 1  #Decrement number of re-connects remaining
                    if message_state[1]>0:
                        s = getNewConnection() #Since UDP is stateless, we must re-connect to the server
                    else:
                        exit()
    except socket.error:
        print("Error -->",socket.error)
        exit()

sendMessage()
