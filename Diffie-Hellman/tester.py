import generator
import math
prime = generator.public_prime()
print("this is our prime: ", prime)

print("now we are are going to test the primative root function with a static prime of 23")

static_prime = 23

print("all of the primitive roots are: ", generator.prim_roots(static_prime))