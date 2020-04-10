#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
						hash_table_insert,
						hash_table_remove,
						hash_table_retrieve,
						hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
	ht = HashTable(16)

	# for i, weight in enumerate(weights):
	# 	hash_table_insert(ht, weight, i)

	# for weight in weights:
	# 	inhand = hash_table_retrieve(ht, weight)
	# 	found = None
	# 	looking = limit - weight
	# 	found = hash_table_retrieve(ht, looking)
	# 	print (20, found, inhand)
	# 	if found != None:
	# 		return (max(found, inhand), min(found, inhand))

	for i in range(length):
		looking = limit - weights[i]
		found = hash_table_retrieve(ht, looking)

		if found == None:
			hash_table_insert(ht, weights[i], i)
		else:
			return max(found, i), min(found, i)


	return None


def print_answer(answer):
	if answer is not None:
		print(str(answer[0] + " " + answer[1]))
	else:
		print("None")
