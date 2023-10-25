import socket

HOST = '127.0.0.1'
PORT = 12345

#create sockect
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the sockect to host and port
server_socket.bind((HOST, PORT))

#Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

#client incoming connection
client_sockect, client_address = server_socket.accept()

print(f"Connection from {client_address} ")

#receive data from the client
data = client_sockect.recv(1024)
print(f"Received: {data.decode('utf-8')}")

#send a response to the client
response = "Hello from the server"
client_sockect.send(response.encode('utf-8'))


client_sockect.close()
server_socket.close()