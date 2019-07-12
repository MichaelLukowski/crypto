from generator import ecdhSystem, X25519, decodeUCoordinate
from os import urandom
import random

# testing of the 
bob = ecdhSystem()
alice = ecdhSystem()

bob_private_key = random.randint(3 , bob.order-1)
alice_private_key = random.randint(3 , alice.order-1)


print("\nBob's Private Key: ")
print(hex(bob_private_key))

bob_public_key = X25519(bob_private_key, 9)
print("\nBob's Public Key: ")
print(hex(bob_public_key))

print("\nAlice's Private Key: ")
print(hex(alice_private_key))

alice_public_key = X25519(alice_private_key, 9)
print("\nAlice's Public Key: ")
print(hex(alice_public_key))

bob_calculated_secret = X25519(bob_private_key, alice_public_key)
alice_calculated_secret = X25519(alice_private_key, bob_public_key)

print("\nHopefully these 2 lines are the same: ")
print(hex(bob_calculated_secret))
print(hex(alice_calculated_secret))