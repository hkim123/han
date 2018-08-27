#! /usr/local/bin/python3
import random

def pop_list(data):
	n = random.randint(0,len(data)-1)
	return data.pop(n)

if __name__ == "__main__":
	data = [1,3,5,6,7]
	while data : print(pop_list(data))
