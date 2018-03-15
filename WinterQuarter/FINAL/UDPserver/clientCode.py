# Send the ping message using UDP
# print the response message from server if any
# calculate and print the round trip time (RTT) in seconds of each packet
# else print Request timed out
from socket import *
import time

HOST, PORT = "localhost", 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
message = raw_input("Input lowercase sentance yo: ")
clientSocket.sendto(message.encode(),(HOST, PORT))
test = True

while test:
    try: 
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        if modifiedMessage:
            print(modifiedMessage.decode())
            test = False
    except timeout:
        print("I give up")
        test = False
    finally:
        clientSocket.close()

#clientSocket.close()
