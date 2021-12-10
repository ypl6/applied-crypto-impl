from Crypto.PublicKey import RSA
import math

# possible to add more and randomly choose 3
RECIPIENTS = [
	"alice", 
	"carol", 
	"danny"
]

def gen_key():
	"""
	Generate (weak) RSA public keys using $e = 3$ for each recipient.
	"""
	for recipient in RECIPIENTS:
		key = RSA.generate(1024, e = 3)
		# == Private key
		# with open(f"keysb/secret/{recipient}.pem", "wb") as priv_key_file:
		# 	priv_key_file.write(key.export_key("PEM"))
		
		# == Public key
		public_key = key.public_key()
		with open(f"keysb/{recipient}.pub", "wb") as pub_key_file:
			pub_key_file.write(public_key.export_key("PEM"))
		
def get_pub_key(name: str):
	"""
	Read the stored public key.
	"""
	with open(f"keys/{name}.pub", "rb") as pub_key_file:
		pub_key = RSA.importKey(pub_key_file.read())
		return pub_key.public_key()

def encrypt(message: int, pub_key: RSA.RsaKey):
	"""
	Textbook RSA encryption without padding.
	"""
	return (message ** pub_key.e) % pub_key.n

def convert_int(message: bytes):
	"""
	Convert string in bytes to integer.
	"""
	return int(message.hex(), 16)