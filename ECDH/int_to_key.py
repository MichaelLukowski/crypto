# from bigfloat import *
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

	Jn1 = key
	i = n
	Ji1 = Jn1
	S = []
	while i > 0:
		# 2.1 Ji = (Ji+1)/256
		Ji = Ji1//256

		# 2.2Ai = Ji+1 − (Ji• 256)
		Ai = Ji1 - (Ji * 256)

		# Si= (ai1, ai2, ai3, ai4, ai5, ai6, ai7, ai8)
		Si = []
		for a in "{0:b}".format(Ai):
			Si.append(int(a))
		while len(Si) != 8:
			Si.insert(0,0)
		S.append(Si)

		Ji1 = Ji
		i -= 1 

	# now we convert binary representations of numbers into hex and append them to a string to return 
	bStr = ""
	for ele in S:
		temp = ""
		for i in ele:
			temp += str(i)

		hexConv = str(hex(int(temp, 2)))
		hexConv = hexConv.replace("x", "0")
		bStr += hexConv[-2:]
		
	hexKey = bStr
	
	return hexKey.encode("utf8")