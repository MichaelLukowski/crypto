import socket
import time
import random
import generator

# establish client socket to listening server
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8085
print("conneting to socket with host: ", host, " and port: ", port)
clientsocket.connect((host, port))

# establish payload, encode it, and send it
payload = 'are you recieving me?'
payload = payload.encode()
print("this is the payload that we are sending to our socket:", payload)
clientsocket.send(payload)

# establish local server to handle request
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8094
print("we are binding the socket on host:", host, " and port: ", port)
serversocket.bind((host, port))
serversocket.listen(5)

# listen for responce from other server
while True:
	connection, address = serversocket.accept()
	buf = connection.recv(64)
	if len(buf) > 0:
		print("recieved this: ", buf.decode())
	break

PUB_PRIME = generator.public_prime()
print("this is the pub key we got: ", PUB_PRIME)
# send the listener the established private key
clientsocket.send(str(PUB_PRIME).encode())

# take a second for the client to acknowledge
time.sleep(1)

PUB_PRIM_ROOT = random.choice(generator.prim_roots(PUB_PRIME))
print("this is the public primative root we got:", PUB_PRIM_ROOT)
# send the listener the primative root modulo prime
clientsocket.send(str(PUB_PRIM_ROOT).encode())

# take a second for the client to acknowloge
time.sleep(1)

# now we generate a private key
# THIS IS THE BIG SECRET THAT NO ONE CAN KNOW
PRIV_KEY = random.randint(10,20) 

PUB_CALC_S = pow(PUB_PRIM_ROOT, PRIV_KEY) % PUB_PRIME

print("this is the pub calc we calculated: ", PUB_CALC_S)
# send the listener the established private key
clientsocket.send(str(PUB_CALC_S).encode())

while True:
	buf = connection.recv(64)
	if len(buf) > 0:
		PUB_CALC_R = int(buf.decode())
		break
print("this is the public calc we recieved: ", PUB_CALC_R)

COMMON_PRIV_KEY = pow(PUB_CALC_R, PRIV_KEY) % PUB_PRIME

print("this is our shared private key: ", COMMON_PRIV_KEY)

print("we are now closing the sockets")

serversocket.close()
clientsocket.close()