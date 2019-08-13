from bigfloat import *
import math



def int_to_byte(key, n):
	"""
	We get a very large number from curve25519 ECDH, This usually coresponds to 64 Bytes long
	Most Ciphers like ChaCha20 that we are using for encoding require a 32 Byte string as a key
	This function is a NIST approved mapping of integer to a n-byte string

	https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf
	Appendix C
		C.1 Integer-to-Byte String Conversion
	"""
	# this is for converting our final key integer into a n byte string key
	if 2**(8*n) < key:
		print("this num is too big")
	Jn1 = key
	i = n
	Ji1 = Jn1
	S = []
	while i > 1:
		# 2.1 Ji = (Ji+1)/256
		Ji = floor(BigFloat(Ji1/256, context=precision(10000)))
		# as of right now Ji can be incorrect due to floating point precision being not good enough for consistant calculations

		# 2.2Ai = Ji+1 − (Ji• 256)
		Ai = Ji1 - (Ji * 256)
		
		Ai = int(Ai)

		print("Ji+1: ", Ji1)
		print("Ji * 256: ", Ji * 256)
		print("mod thing: ", Ji1 % 256)
		print("Ji: ", Ji)
		print("Ai: ", Ai)

		if Ai < 0:
			print("no idea how we got a negative on this one???")
			Ai = abs(Ai)

		# Si= (ai1, ai2, ai3, ai4, ai5, ai6, ai7, ai8)
		Si = []


		for a in "{0:b}".format(Ai)[-8:]:
			Si.append(int(a))
		S.append(Si)

		Ji1 = Ji
		i -= 1 

	bStr = ""
	for ele in S:
		temp = ""
		for i in ele:
			temp += str(i)
		bStr += hex(int(temp, 2))[-2:]
		# for i in ele:
		# 	bStr += str(i)
	print(bStr)
	hexKey = bStr
	# hexKey = hex(int(bStr, 2))
	
	return hexKey