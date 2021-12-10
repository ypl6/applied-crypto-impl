from flask import Flask, request
from utils import *

app = Flask(__name__)
	
MESSAGE = "Aphrodite, subtle of soul and deathless.".encode("utf-8")
MESSAGE_INT = convert_int(MESSAGE)
MESSAGE_STR = MESSAGE.decode('utf-8')

@app.route("/message/<path:name>", methods=["GET"])
def get_message(name: str):
	try:
		pub_key = get_pub_key(name)
	except FileNotFoundError:
		return {"error": "recipient's public key does not exist"}
		
	ciphertext = encrypt(MESSAGE_INT, pub_key)
	res = {
		"recipient": name,
		"n": pub_key.n,
		"e": pub_key.e,
		"ciphertext": f"{ciphertext}",
	}
	return res