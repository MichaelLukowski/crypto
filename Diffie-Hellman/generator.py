import sievePrimes
import random

def gcd(a,b):
	while a != b:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a



def public_prime():
	# this is wrong we need to generat the prime number and a random primative root from that prime number

	# establish a list of primes and pick one of them as our private key for exchange 
	primes = sievePrimes.sievesMethod(200)
	pub_key = random.choice(primes)
	return pub_key

def public_generator():
	# we need to define a generator in terms of the public prime
	return 0

def primitive_root(modulo):
	required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
	for g in range(1, modulo):
		actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
		if required_set == actual_set:
			return g