# %%
import math
import json
import binascii
from urllib.request import urlopen
from functools import reduce
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


def crt(n, a):
    """
    Calculate by Chinese Remainder Theorem.
    """
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# %%
def find_m():
    """
    Given $e = 3$ samples, construct lists $c$, $n$ where $c_i \equiv m^{e} (mod\ n_i)$. Then, use CRT to find $m$.
    """
    n = []
    c = []
    samples = get_res()
    for sample in samples:
        n.append(sample.n)
        c.append(sample.ciphertext)
    crtd = crt(n, c)  # Refers to $m^3$
    m = round(math.pow(crtd, 1/3))
    return m


print(find_m())
