#!/usr/bin/python

filename = input("Please enter your file name: ")

with open(filename, 'r') as f:
	lines = f.readlines()

l = list(line.rstrip('\n') for line in lines)

measurements_count = 0
while len(l) != 1:
	if l[0] < l[1]:
		measurements_count += 1
	del(l[0])
else:
	print(f"There are {measurements_count} measurments larger than the previous measurment.")

		
