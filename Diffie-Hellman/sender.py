import socket
import time
import random
import sievePrimes
import generator

# establish client socket to listening server
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8089
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
port = 8093
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

pub_key = generator.public_prime()
print("this is the pub key we got: ", pub_key)

# send the listener the established private key
clientsocket.send(pub_key.encode())

# now we generate a private key
PRIV_KEY = random.randint(1,20) 