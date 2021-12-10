from Crypto.PublicKey import RSA
import math
import gmpy2

# possible to add more and randomly choose 3
RECIPIENTS = [
	"alice", 
	"carol", 
	"danny",
]

def gen_keys_small_n():
	"""
	Generate (weak) RSA public keys using $e = 3$ for each recipient.
	"""
	e = 3
	small_n = [37, 113, 209] # size e
	for i in range(len(RECIPIENTS)):
		key = RSA.construct((small_n[i], e))
		public_key = key.public_key()
		with open(f"keys_small_n/{RECIPIENTS[i]}.pub", "wb") as pub_key_file:
			pub_key_file.write(public_key.export_key("PEM"))

def get_pub_key(name: str):
	"""
	Read the stored public key.
	"""
	with open(f"keys_small_n/{name}.pub", "rb") as pub_key_file:
		print(pub_key_file)
		pub_key = RSA.importKey(pub_key_file.read())
		return pub_key.public_key()

def encrypt(message: int, pub_key: RSA.RsaKey):
	"""
	Textbook RSA encryption without padding.
	"""
	c = (message ** pub_key.e) % pub_key.n
	return c

def convert_int(message: bytes):
	"""
	Convert string in bytes to integer.
	"""
	return int(message.hex(), 16)