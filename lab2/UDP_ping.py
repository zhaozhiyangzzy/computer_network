from threading import Timer
import time
from socket import *
import datetime
def UDP_ping():
    count = 0
    serverName = "47.94.129.112"
    serverPort = 50021
    
    while count<10:
        send_time = datetime.datetime.now()
        send_time_s = datetime.datetime.strftime(send_time,'%H:%M:%S')
        print('send_time_s=',send_time_s)
        clientSocket = socket(AF_INET,SOCK_DGRAM)
        message = "zzy"
        clientSocket.sendto(message.encode(),(serverName,serverPort))
        try:
            clientSocket.settimeout(1)
            modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
            #todo rtt=response_time - send_time_s
            print(modifiedMessage.decode())
            count = count +1
        except:
            count = count+1
            print("timeout")
        clientSocket.close()
UDP_ping()

