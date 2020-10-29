#This is a program to print the cartesian product of numbers.

import itertools
from itertools import product

repeat = int(input('How many possible combinations do you want? > '))

def cart_product():
	all_digits = []
	for value in product(range(0,10),repeat=repeat):
		all_digits.append(''.join(map(str,value)))
	print(all_digits)

cart_product()
