    from socket import * 
import sys

serverPort = 50001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(2)
#print('The server is ready to receive')


while True:
    print('Ready to serve...')
    connectionSocket,addr=serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        #print("endline")
        filename=message.split()[1]
        #print("filename is ",filename)
        f = open(filename[1:])
        outputdata = f.read()
        Content_Length="Connection-Length: "+str(len(outputdata))+"\r\n"
        print("content_length",Content_Length)

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Connection: close\r\n".encode())
        connectionSocket.send(Content_Length.encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        
        #connectionSocket.send("\r\n".encode())

        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        print("some error happen\n")
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        #connectionSocket.send("Connection: close\r\n".encode())
        #connectionSocket.send("\r\n\r\n".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()


    
