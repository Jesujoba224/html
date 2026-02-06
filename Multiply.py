"""Multiply two integers using two methods:

- `multiply_one_iteration(n, m)` uses the built-in multiplication (one operation).
- `multiply_n_iterations(n, m)` uses repeated addition (n iterations).

The script also supports CLI usage:
  python Multiply.py 5 3
or interactive input when no args provided.
"""

import sys
from typing import Tuple


def multiply_one_iteration(n: int, m: int) -> int:
	"""Return product using a single multiplication operation."""
	return n * m


def multiply_n_iterations(n: int, m: int) -> int:
	"""Return product by repeated addition using |n| iterations.

	Handles negative values for `n` and `m` correctly.
   """
	sign = -1 if (n < 0) ^ (m < 0) else 1
	a, b = abs(n), abs(m)
	result = 0
	for _ in range(a):
		result += b
	return sign * result


def parse_args(argv: list) -> Tuple[int, int]:
	if len(argv) >= 3:
		try:
			return int(argv[1]), int(argv[2])
		except ValueError:
			pass
	# fallback to interactive input
	while True:
		try:
			n = int(input('Enter N (integer): ').strip())
			m = int(input('Enter M (integer): ').strip())
			return n, m
		except ValueError:
			print('Invalid input; please enter integers.')


if __name__ == '__main__':
	n, m = parse_args(sys.argv)
	print(f'N = {n}, M = {m}')
	one = multiply_one_iteration(n, m)
	many = multiply_n_iterations(n, m)
	print('multiply_one_iteration ->', one)
	print('multiply_n_iterations ->', many)
