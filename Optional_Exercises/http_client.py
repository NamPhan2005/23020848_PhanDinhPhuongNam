import socket
import sys

if len(sys.argv) != 4:
    print("Usage: python http_client.py <server_host> <server_port> <filename>")
    sys.exit()

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((server_host, server_port))

request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
clientSocket.send(request.encode())

response = b""
while True:
    chunk = clientSocket.recv(1024)
    if not chunk:
        break
    response += chunk

print("From Server:\n")
print(response.decode())

clientSocket.close()
