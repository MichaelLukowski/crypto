import json
from Crypto.Cipher import ChaCha20
from base64 import b64encode, b64decode

def encode_chacha20(ecdh_key, message):
	message = message.encode()

	cipher = ChaCha20.new(key=ecdh_key)

	cipherText = cipher.encrypt(message)

	nonce = b64encode(cipher.nonce).decode('utf-8')
	ct = b64encode(cipherText).decode('utf-8')
	result = json.dumps({'nonce':nonce, 'cipherText':ct})

	return result
	

def decode_chacha20(ecdh_key, encoded_message):
	try:
		b64 = json.loads(encoded_message)
		nonce = b64decode(b64['nonce'])
		cipherText = b64decode(b64['cipherText'])
		
		cipher = ChaCha20.new(key=ecdh_key, nonce=nonce)
		plainText = cipher.decrypt(cipherText)

		return plainText.decode()

	except:
		return "there was an error with the decryption"