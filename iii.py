import math
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(raw_input("Choose a number: "))

a1 = []

for i in a:
	if i < num:
		a1.append(i)

print (a1)
