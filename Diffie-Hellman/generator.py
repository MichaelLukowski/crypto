import sievePrimes
import random

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

def public_generator():
	# we need to define a generator in terms of the public prime
	return 0

def primitive_root(modulo):
	# create a required set to find coprime numbers to the given prime number
	required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
	for g in range(1, modulo):
		# then we loop through
		actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
		if required_set == actual_set:
			return g

def all_primitive_roots(root, prime):
	roots = []
	for a in range(1, (prime - 1)):
		if gcd(a, prime-1) == 1:
			print("this is the power", pow(root, a))
			roots.append(pow(root, a))
	return(roots)


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
