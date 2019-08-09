import sievePrimes
import random
import numpy as np
import decimal
import math
import sys

# Establishment of global variables
P = 2 ** 255 - 19
A24 = 121665

class ecdhSystem:
	"""
	This is an Eliptic Curve system based on Curve 25519

	the eliptic curve diffie hellman key exchange uses this sextuple to describe the key exchange
	p prime (specifies the size of the finite field)
	coefficients a and b of the eliptic curve equation
	base point G that generates our subgroup
	n order of the subgroup
	h cofactor of the subgroup
	"""
	def __init__(self):
		self.prime = (2**255) - 19
		self.a = 486662
		self.b = 1
		self.gX = 9
		self.gY = 14781619447589544791020593568409986887264606134616475288964881837755586237401
		self.order = (2**252) + 27742317777372353535851937790883648493
		self.cofactor = 8

def decodeLittleEndian(b, bits):
	return sum([b[i] << 8*i for i in range((bits+7)/8)])

def decodeUCoordinate(u, bits):
	u_list = [ord(b) for b in u]
	# Ignore any unused bits.
	if bits % 8:
	   u_list[-1] &= (1<<(bits%8))-1
	return decodeLittleEndian(u_list, bits)

def encodeUCoordinate(u, bits):
	u = u % p
	return ''.join([chr((u >> 8*i) & 0xff) for i in range((bits+7)/8)])

def decodeScalar25519(k):
	k_list = [ord(b) for b in k]
	k_list[0] &= 248
	k_list[31] &= 127
	k_list[31] |= 64
	return decodeLittleEndian(k_list, 255)

def cswap(swap, x_2, x_3):
	dummy = swap * ((x_2 - x_3) % P)
	x_2 = x_2 - dummy
	x_2 %= P
	x_3 = x_3 + dummy
	x_3 %= P
	return (x_2, x_3)

def X25519(k, u):
	x_1 = u
	x_2 = 1
	z_2 = 0
	x_3 = u
	z_3 = 1
	swap = 0

	for t in reversed(range(255)):
		k_t = (k >> t) & 1
		swap ^= k_t
		x_2, x_3 = cswap(swap, x_2, x_3)
		z_2, z_3 = cswap(swap, z_2, z_3)
		swap = k_t

		A = x_2 + z_2
		A %= P

		AA = A * A
		AA %= P

		B = x_2 - z_2
		B %= P

		BB = B * B
		BB %= P

		E = AA - BB
		E %= P

		C = x_3 + z_3
		C %= P

		D = x_3 - z_3
		D %= P

		DA = D * A
		DA %= P

		CB = C * B
		CB %= P

		x_3 = ((DA + CB) % P)**2
		x_3 %= P

		z_3 = x_1 * (((DA - CB) % P)**2) % P
		z_3 %= P

		x_2 = AA * BB
		x_2 %= P

		z_2 = E * ((AA + (A24 * E) % P) % P)
		z_2 %= P

	x_2, x_3 = cswap(swap, x_2, x_3)
	z_2, z_3 = cswap(swap, z_2, z_3)

	return (x_2 * pow(z_2, P - 2, P)) % P
	

