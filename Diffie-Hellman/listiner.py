import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8089
print("we are binding the socket on host:", host, " and port: ", port)
serversocket.bind((host, port))
serversocket.listen(5)

while True:
	connection, address = serversocket.accept()
	buf = connection.recv(64)
	if len(buf) > 0:
		print("recieved this: ", buf.decode())
		break

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.settimeout(10)
host = 'localhost'
port = 8093
print("conneting to socket with host: ", host, " and port: ", port)

clientsocket.connect((host, port))

print("now we are going to send back a message")

payload = "we recieved you and are waiting for a public key"
payload = payload.encode()
clientsocket.send(payload)

print("now we wait for key")

# now we listen for a public key to be sent over
while True:
	buf = connection.recv(64)
	if len(buf) > 0:
		print("recieved this: ", buf.decode())
		PUB_KEY = int(buf.decode())
		break
print("we now have a public key of: ", PUB_KEY)
		