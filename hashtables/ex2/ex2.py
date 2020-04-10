#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
						hash_table_insert,
						hash_table_remove,
						hash_table_retrieve,
						hash_table_resize)


class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination


def reconstruct_trip(tickets, length):
	ht = HashTable(length)
	route = [None] * length

	for t in tickets:
		hash_table_insert(ht, t.source, t.destination)

	count = 0

	prev = "NONE"
	while count < length:
		chk = hash_table_retrieve(ht, prev)
		if chk == "NONE":
			break
		else:
			route[count] = chk
			prev = route[count]
			count += 1
	print(33, route[:-1])
	return route[:-1]

