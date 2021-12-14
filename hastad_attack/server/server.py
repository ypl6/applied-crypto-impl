from flask import Flask, request
from utils import *

app = Flask(__name__)
	
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
	ciphertext = textbook_encrypt(APHRODITE.raw_int, pub_key)
	res = {
		"recipient": name,
		"n": pub_key.n,
		"e": pub_key.e,
		"ciphertext": ciphertext,
	}
	return res

@app.route("/message/<path:name>/pad", methods=["GET"])
def get_padded_message(name: str):
	try:
		pub_key = get_pub_key(name)
	except FileNotFoundError:
		return {"error": "recipient's public key does not exist"}
	ciphertext = simple_pad_encrypt(APHRODITE.raw_int, pub_key)
	res = {
		"recipient": name,
		"n": pub_key.n,
		"e": pub_key.e,
		"ciphertext": ciphertext,
	}
	return res