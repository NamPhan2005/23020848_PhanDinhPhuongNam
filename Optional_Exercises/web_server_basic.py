from socket import *
from threading import Thread

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        with open(filename[1:], 'r') as f:
            outputdata = f.read()
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n404 Not Found".encode())
    finally:
        connectionSocket.close()

def main():
    serverPort = 6789
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print("Multithreaded Web Server is running...")

    while True:
        connectionSocket, addr = serverSocket.accept()
        thread = Thread(target=handle_client, args=(connectionSocket,))
        thread.start()

if __name__ == '__main__':
    main()
