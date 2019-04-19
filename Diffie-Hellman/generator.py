import sievePrimes

def public_prime():
	# this is wrong we need to generat the prime number and a random primative root from that prime number

	# establish a list of primes and pick one of them as our private key for exchange 
	primes = sievePrimes.sievesMethod(200)
	pub_key = str(random.choice(primes))

def public_generator():
	# we need to define a generator in terms of the public prime