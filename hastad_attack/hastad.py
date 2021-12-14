# %%
import json
import binascii
from sympy.ntheory.modular import crt
from gmpy2 import iroot
from urllib.request import urlopen
from dataclasses import dataclass

@dataclass
class TextSample:
	n: int
	ciphertext: int

# %%
def get_res():
	"""
	Retrieve data from server.
	"""
	samples = []
	base_url = "http://127.0.0.1:5000/message/"
	rep_list = json.load(urlopen(base_url))["recipients"]
	for r in rep_list:
		url = urlopen(base_url + r)
		data = json.load(url)
		sample = TextSample(n=data["n"], ciphertext=data["ciphertext"])
		samples.append(sample)
	return samples

# %%
def hastad_unpadded():
	"""
	Given $e = 3$ samples, construct lists $c$, $n$ where $c_i \equiv m^{e} (mod\ n_i)$. Then, use CRT to find $m$.
	"""
	e = 3
	n = []
	c = []
	samples = get_res()
	for sample in samples:
		n.append(sample.n)
		c.append(sample.ciphertext)
	result, mod = crt(n, c)  # result refers to $m^3$
	value, valid  = iroot(result, e)
	if valid:
		return value

# %%
unpadded = int(hastad_unpadded())
print(unpadded)
print(binascii.unhexlify(hex(unpadded)[2:].strip("L")))

# %%
# padded = int(hastad_padded())
# print(padded)
# print(binascii.unhexlify(hex(padded)[2:].strip("L")))