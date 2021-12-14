from utils import *

def test_textbook_enc():
	for recipient in RECIPIENTS:
		pub_key = get_pub_key(recipient)
		ciphertext = textbook_encrypt(APHRODITE.raw_int, pub_key)
		print(ciphertext, "\n")

test_textbook_enc()