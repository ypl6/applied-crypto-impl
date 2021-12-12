from flask import Flask, request
from utils import *

app = Flask(__name__)
	
# MESSAGE = "Aphrodite, subtle of soul and deathless.".encode("utf-8")
# MESSAGE_INT = convert_int(MESSAGE)
SHORT_MESSAGE = 25 # $m$ should be less than all $n_i$

@app.route("/message/", methods=["GET"])
def get_list():
	res = {
		"recipients": RECIPIENTS
	}
	return res

@app.route("/message/<path:name>", methods=["GET"])
def get_message(name: str):
	try:
		pub_key = get_pub_key(name)
	except FileNotFoundError:
		return {"error": "recipient's public key does not exist"}
		
	ciphertext = encrypt(SHORT_MESSAGE, pub_key)
	res = {
		"recipient": name,
		"n": pub_key.n,
		"e": pub_key.e,
		"ciphertext": ciphertext,
	}
	return res