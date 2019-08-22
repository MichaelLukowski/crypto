from generator import ecdhSystem, X25519, decodeUCoordinate
from int_to_key import int_to_byte
from os import urandom
import sys
from base64 import b64encode, b64decode
import json
from Crypto.Cipher import ChaCha20
import random

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
message = "I wonder if this requires some special length"
message = message.encode()


# Conversion of 64 length key to 32 length key
bob_byteLimitKey = int_to_byte(bob_calculated_secret, 16)

cipher = ChaCha20.new(key=bob_byteLimitKey)
# obj = AES.new(hex(bob_calculated_secret), AES.MODE_CBC, "This is an IV446")

cipherText = cipher.encrypt(message)

nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(cipherText).decode('utf-8')
result = json.dumps({'nonce':nonce, 'cipherText':ct})
print(result)

try:
	b64 = json.loads(result)
	nonce = b64decode(b64['nonce'])
	cipherText = b64decode(b64['cipherText'])
	alice_byteLimitKey = int_to_byte(alice_calculated_secret, 16)
	newCipher = ChaCha20.new(key=alice_byteLimitKey, nonce=nonce)
	plaintext = newCipher.decrypt(cipherText)
	print("the message was: ", plaintext.decode())
except:
    print("Incorrect decryption")

