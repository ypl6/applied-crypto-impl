from Crypto.PublicKey import RSA
from dataclasses import dataclass
import random

def gen_keys():
	"""
	Generate (weak) RSA public keys using $e = 3$ for each recipient.
	This is not called when handling requests.
	"""
	for i in range(len(RECIPIENTS)):
		key = RSA.generate(1024, e = 3)
		public_key = key.public_key()
		with open(f"keys/{RECIPIENTS[i].name}.pub", "wb") as pub_key_file:
			pub_key_file.write(public_key.export_key("PEM"))

def get_pub_key(name: str):
	"""
	Read the stored public key.
	"""
	with open(f"keys/{name}.pub", "rb") as pub_key_file:
		pub_key = RSA.importKey(pub_key_file.read())
		return pub_key.public_key()

def textbook_encrypt(message: int, pub_key: RSA.RsaKey):
	"""
	Textbook RSA encryption without padding.
	"""
	c = pow(message, pub_key.e, pub_key.n)
	return c
	
def simple_pad_encrypt(message: int, pub_key: RSA.RsaKey):
	"""
	Textbook RSA encryption with weak padding.
	"""
	something_to_add = random.randint(1, 2048)
	print("something_to_add:", something_to_add)
	c = pow(message + something_to_add, pub_key.e, pub_key.n)
	return c

def convert_int(message: bytes):
	"""
	Convert string in bytes to integer.
	"""
	return int(message.hex(), 16)

@dataclass
class Message:
	raw_int: int

# aphrodite = "Aphrodite, subtle of soul and deathless. Daughter of God, weaver of wiles, I pray thee."
# aphrodite_int = convert_int(aphrodite.encode("utf-8"))
APHRODITE = Message(raw_int=84037726152314829912290806586038319621521592711564798488513299671306110446562137161591546039327051431408754387718625452506855330110874560579056026965209996080419808088002401111444342694275165783209474110350638)

RECIPIENTS = ["alice", "carol", "danny"]


