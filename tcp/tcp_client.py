import socket, sys


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"
CLIENT_ID = sys.argv[1]
CLIENT_DELAY = int(sys.argv[2])
CLIENT_PING_MESSAGE_COUNT = int(sys.argv[3])

def sendContent(message,s=None):
    global CLIENT_PING_MESSAGE_COUNT
    if not s:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(message.encode())
        sendContent(get_user_message(),s)
    while CLIENT_PING_MESSAGE_COUNT > 0 : #len(message)>0 and s.fileno()>=0:
        s.send(message.encode())
        data = s.recv(BUFFER_SIZE)
        print(data.decode())
        CLIENT_PING_MESSAGE_COUNT -= 1
        if CLIENT_PING_MESSAGE_COUNT > 0:
            sendContent(get_user_message(),s)
    if s.fileno()>=0:
        #Close connection only once after terminating message
        print("Closing connection")
        s.close()
    return None


def get_user_message():
    message = input("You:")
    return CLIENT_ID+","+str(CLIENT_DELAY)+","+str(CLIENT_PING_MESSAGE_COUNT)+","+message


print("Name : ",CLIENT_ID,"Delay : ",CLIENT_DELAY,"Message Count : ",CLIENT_PING_MESSAGE_COUNT)
sendContent(CLIENT_ID+","+str(CLIENT_DELAY)+","+str(CLIENT_PING_MESSAGE_COUNT)+","+"Connect to Server")
