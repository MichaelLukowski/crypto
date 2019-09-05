from generator import ecdhSystem, X25519, decodeUCoordinate
from int_to_key import int_to_byte
from os import urandom
import sys
from base64 import b64encode, b64decode
import json
from Crypto.Cipher import ChaCha20
import random
from cypher import encode_chacha20, decode_chacha20

# testing of the 
bob = ecdhSystem()
alice = ecdhSystem()

bob_private_key = random.randint(3 , bob.order-1)
alice_private_key = random.randint(3 , alice.order-1)


print("\nBob's Private Key: ")
print(hex(bob_private_key))

bob_public_key = X25519(bob_private_key, bob.gX)
print("\nBob's Public Key: ")
print(hex(bob_public_key))

print("\nAlice's Private Key: ")
print(hex(alice_private_key))

alice_public_key = X25519(alice_private_key, alice.gX)
print("\nAlice's Public Key: ")
print(hex(alice_public_key))

bob_calculated_secret = X25519(bob_private_key, alice_public_key)
alice_calculated_secret = X25519(alice_private_key, bob_public_key)

print("\nHopefully these 2 lines are the same: ")
print(hex(bob_calculated_secret))
print(hex(alice_calculated_secret))
print("\n")


if bob_calculated_secret != alice_calculated_secret:
	print("something very wrong has happened with these keys")

print("\nNow that we have the same secret we are going to encrypt using ChaCha20")
message = "this is a really secret message!!"



# Conversion of 64 length key to 32 length key
bob_byteLimitKey = int_to_byte(bob_calculated_secret, 16)
alice_byteLimitKey = int_to_byte(alice_calculated_secret, 16)


encoded = encode_chacha20(bob_byteLimitKey, message)
print(encoded)

decoded = decode_chacha20(alice_byteLimitKey, encoded)

print("this is the decoded message:")
print(decoded)

