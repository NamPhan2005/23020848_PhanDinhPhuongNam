import socket
import threading

def handle_client(connectionSocket, addr):
    print(f"Connection from {addr}")
    sentence = connectionSocket.recv(1024).decode()
    print(f"Received: {sentence}")
    response = sentence.upper()
    connectionSocket.send(response.encode())
    connectionSocket.close()

def main():
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print("Threaded TCP Server ready...")

    while True:
        connectionSocket, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        thread.start()

if __name__ == "__main__":
    main()
