import socket
import time
import random

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8085
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
port = 8094
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
		PUB_PRIME = int(buf.decode())
		break
print("we now have a public key of: ", PUB_PRIME)
		
while True:
	buf = connection.recv(64)
	if len(buf) > 0:
		PUB_PRIM_ROOT = int(buf.decode())
		break
print("we now have a public primative root of: ", PUB_PRIM_ROOT)

while True:
	buf = connection.recv(64)
	if len(buf) > 0:
		PUB_CALC_R = int(buf.decode())
		break
print("this is the public calc we recieved: ", PUB_CALC_R)

# now we generate a private key
PRIV_KEY = random.randint(21,40) 

PUB_CALC_S = pow(PUB_PRIM_ROOT, PRIV_KEY) % PUB_PRIME
print("this is the pub calc we calculated: ", PUB_CALC_S)

# send the listener the established private key
clientsocket.send(str(PUB_CALC_S).encode())

COMMON_PRIV_KEY = pow(PUB_CALC_R, PRIV_KEY) % PUB_PRIME

print("this is our shared private key: ", COMMON_PRIV_KEY)

print("we are now closing the sockets")

serversocket.close()
clientsocket.close()