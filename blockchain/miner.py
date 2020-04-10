import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
	"""
	Multi-Ouroboros of Work Algorithm
	- Find a number [PRIME] such that the last five digits of hash(p) are equal
	to the first five digits of hash([PRIME])
	- IE:  last_hash: ...AE912345, new hash 12345888...
	- p is the previous proof, and [PRIME] is the new proof
	- Use the same method to generate SHA-256 hashes as the examples in class
	"""

	start = timer()

	print("Searching for next proof")
	
	#  TODO: Your code here
	proof = random.random()
	while not valid_proof(last_proof, proof):
		proof = random.random()

	print("Proof found: " + str(proof) + " in " + str(timer() - start))
	return proof


def valid_proof(last_proof, proof):
	"""
	Validates the Proof:  Multi-ouroborus:  Do the last five characters of
	the hash of the last proof match the first five characters of the hash
	of the new proof?

	IE:  last_hash: ...AE912345, new hash 12345E88...
	"""

	last_proof_prep = f"{last_proof}".encode()
	last_hash = hashlib.sha256(last_proof_prep).hexdigest()

	# guess = f"{last_hash}{proof}".encode()
	guess = f"{proof}".encode()
	guess_hash = hashlib.sha256(guess).hexdigest()

	# print(51, last_hash[-5:], guess_hash[:5])
	# print(52, last_hash[-5:] == guess_hash[:5])

	return last_hash[-5:] == guess_hash[:5]


	

	

if __name__ == "__main__":
	# What node are we interacting with?
	#
	# 	LETS GET THE CRUFT OUTTA THE WAY.
	#
	# if len(sys.argv) > 1:
	#     node = sys.argv[1]
	# else:
	
	# REAL NODE
	node = "https://lambda-coin.herokuapp.com/api"

	# # TESTING ONLY 
	# node = "https://lambda-coin-test-1.herokuapp.com/api"

	coins_mined = 0

	# Load or create ID
	f = open("my_id.txt", "r")
	id = f.read()
	print("ID is", id)
	f.close()

	if id == "NONAME\n":
		print("ERROR: You must change your name in `my_id.txt`!")
		exit()


	# ~~Run forever until interrupted~~
	# No.

	count = 0

	while True:
		# Get the last proof from the server
		r = requests.get(url=node + "/last_proof")

		data = r.json()		# incoming float
		
		new_proof = proof_of_work(data.get("proof"))

		post_data = {"proof": new_proof, "id": id}

		r = requests.post(url=node + "/mine", json=post_data)
		data = r.json()
		if data.get("message") == "New Block Forged":
			coins_mined += 1
			print("Total coins mined: " + str(coins_mined))
		else:
			print(data.get("message"))
		
		# count += 1
		
		# if count > 10:
		# 	break
