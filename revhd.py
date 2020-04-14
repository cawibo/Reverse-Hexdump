#!/usr/bin/env python3

"""A simple program that reverses a hexdump into its original state.

The hexdump must follow the format:
	<index>: raw data |ASCII content|

Author: Caroline Borg
Date: 14/04/2020
"""

from parse import *

HEXDUMP_PATTERN = "{}:{}|{}|"

def reverse(hexdump):
	"""Returns a reversed hexdump as a bytearray.

	Parameters:
		hexdump (str): content of a hexdump file.
	"""
	res = []
	for line in hexdump.split("\n"):
		try:
			# extract the second matching group and strip whitespace
			data = parse(HEXDUMP_PATTERN, line)[1].strip()

		except:
			pass

		else:
			for byte in data.split():
				res.append(byte)

	return bytearray.fromhex("".join(res))

if __name__ == "__main__":
	import sys

	if len(sys.argv) == 1:
		print("""Use the following format: revhd <hexdump_filename> [reversed_filename]""")
		sys.exit(0)
	else:
		with open(sys.argv[1]) as _f:
			res = reverse(_f.read())

		if len(sys.argv) == 2:
			print(res)
		else:
			with open(sys.argv[2], 'wb') as _f:
				_f.write(res)