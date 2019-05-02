import generator

prime = generator.public_prime()
print("this is our prime: ", prime)
root = generator.primitive_root(prime)
print("this is our primative root: ", root)

print("now we are are going to test the primative root function with a static prime")

static_prime = 23

for i in range(10):
	print(generator.primitive_root(static_prime))