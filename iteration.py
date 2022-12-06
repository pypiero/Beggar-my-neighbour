#!/usr/bin/env python3
from itertools import combinations


def main():
	a = combinations('AAAAAAA',4)
	b = [''.join(i) for i in a]
	print(b)

main()

# usefull resource: https://docs.python.org/3/library/itertools.html