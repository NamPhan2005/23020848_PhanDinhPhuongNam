from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Web server is ready to serve on port", serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:], 'r')
        outputdata = f.read()

        header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())
    except IOError:
        error_msg = 'HTTP/1.1 404 Not Found\r\n\r\n404 Not Found'
        connectionSocket.send(error_msg.encode())
    finally:
        connectionSocket.close()
