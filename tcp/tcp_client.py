import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def sendContent(message,s=None):
    if not s:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
    while len(message)>0 and s.fileno()>=0:
        s.send(message.encode())
        data = s.recv(BUFFER_SIZE)
        print(data.decode())
        sendContent(get_user_message(),s)
    if s.fileno()>=0:
        #Close connection only once after terminating message
        print("Closing connection")
        s.close()
    return None


def get_user_message():
    message = input("You:")
    return message


sendContent(get_user_message())
