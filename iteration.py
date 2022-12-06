#!/usr/bin/env python3
from itertools import combinations


def main():
	list1 = '11110000222233334444'
	a = combinations(list1,20)
	print(len(list1))
	b = [''.join(i) for i in a]
	print(len(b))

main()

# usefull resource: https://docs.python.org/3/library/itertools.html