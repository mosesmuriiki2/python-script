import socket

HOST = '127.0.0.1'
PORT = 12345


#create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to the server

client_socket.connect((HOST, PORT))


#Send message to the server
message = "Hello from the client"
client_socket.send(message.encode('utf-8'))

#Receive a response from the server
response = client_socket.recv(1024)
print(f"received from server : {response.decode('utf-8')}")

#close connection
client_socket.close()
