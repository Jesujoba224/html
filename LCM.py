"""LCM.py

Simple program to compute the Lowest Common Multiple (LCM)
of two integers using the greatest common divisor (GCD).

Usage:
	python "PRACTICE HTML/LCM.py"

When run directly the script prompts for two integers and
prints their GCD and LCM with a brief explanation.

Functions provided:
	- gcd(a, b): returns greatest common divisor using Euclid's algorithm
	- lcm(a, b): returns lowest common multiple using the relation
				  lcm(a, b) = abs(a*b) // gcd(a, b) (with lcm(0, b) == 0)
"""

from typing import Tuple


def gcd(a: int, b: int) -> int:
	"""Return the greatest common divisor of a and b (non-negative).

	Uses the iterative Euclidean algorithm. Always returns a non-negative int.
	"""
	a, b = abs(a), abs(b)
	while b:
		a, b = b, a % b
	return a


def lcm(a: int, b: int) -> int:
	"""Return the lowest common multiple of a and b.

	If either input is 0, returns 0 (LCM defined as 0 for zero inputs here).
	"""
	if a == 0 or b == 0:
		return 0
	return abs(a // gcd(a, b) * b)


def parse_pair(user_input: str) -> Tuple[int, int]:
	"""Parse two integers from a string separated by space or comma."""
	sep = ',' if ',' in user_input else None
	parts = user_input.split(sep)
	parts = [p.strip() for p in parts if p.strip()]
	if len(parts) != 2:
		raise ValueError('Please provide exactly two integers.')
	return int(parts[0]), int(parts[1])


def main() -> None:
	print('Find the Lowest Common Multiple (LCM) of 2 integers')
	print('Enter two integers separated by space or comma (e.g. "12 18" or "12,18").')
	try:
		s = input('Numbers: ').strip()
		a, b = parse_pair(s)
	except Exception as e:
		print('Invalid input:', e)
		return

	g = gcd(a, b)
	m = lcm(a, b)

	print(f'GCD({a}, {b}) = {g}')
	print(f'LCM({a}, {b}) = {m}')
	print('\nHow it works:')
	print(' - GCD is found via the Euclidean algorithm.')
	print(' - LCM is computed as |a*b| / GCD(a,b).')


if __name__ == '__main__':
	main()

