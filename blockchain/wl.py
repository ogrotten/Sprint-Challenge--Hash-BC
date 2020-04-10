import random

first = "1234599999"
second = str(random.random())
count = 0

spaces = 5

while first[:spaces] != second[-spaces:]:
	first = "1234599999"
	second = str(random.random())
	count += 1
	if count > 1000000:
		print("1m break")
		break
print (count, first[:spaces], second[-spaces:])