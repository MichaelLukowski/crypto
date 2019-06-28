import sievePrimes
import random
import math


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
		self.generatorPoint = 9
		self.order = (2**252) + 27742317777372353535851937790883648493
		self.cofactor = 8

		

def gcd(a,b):
	if b:
		return gcd(b, a % b)
	else:
		return a;

def public_prime():
	# this is wrong we need to generat the prime number and a random primative root from that prime number

	# establish a list of primes using sieves method and pick one of them as our private key for exchange 
	primes = sievePrimes.sievesMethod(200)
	pub_key = random.choice(primes)
	return pub_key

def prim_roots(prime):
	roots = []

	for r in range(2, prime):
		a = 1
		k = r % prime
		while k > 1:
			a += 1
			k = k * r
			k = k % prime
		if a == (prime -1):
			roots.append(r)

	return roots
