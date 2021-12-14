# README

A simplified setup for testing Hastad's Broadcast Attack at the simplest form (i.e. $e = 3$ and $m$ is not padded).

## Environment

- Run `$ pip install -r requirements.txt`

## Server

- `$ flask run` to start the server at port 5000
- Send `GET` request to `http://127.0.0.1:5000/message/` for list of recipients available
- Send `GET` request to `http://127.0.0.1:5000/message/<recipient>` for the corresponding ciphertext

## Eve

- Run `hastad.py` (IPython available)
