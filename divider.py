#!/usr/bin/env python3

from sys import argv

defaults = [ 100, 150, 200, 250, 330, 470, 680, 1000, 1200, 1500, 2200, 4700, 10000, 22000, 33000, 47000, 100000, 220000, 1000000 ]

def gen_pairs(values: list, ratio: float) -> list:
	"""Make a list of dividend, divisor pairs matching the ratio."""
	out = []
	for value in values:
		out.append((value * ratio, value))
		out.append((value, value / ratio))
	return out

def closest(legal: list, value: float) -> float:
	"""Find the closest element to value in legal."""
	cur = None
	for x in legal:
		if cur == None or abs(value-x) < abs(value-cur):
			cur = x
	return cur

def closest_divider(values: list, ratio: float, n=1) -> tuple:
	"""Find the closest possible resistor divider ratio using given values."""
	ideal = gen_pairs(values, ratio)
	real  = []
	for x, y in ideal:
		real.append((closest(values, x), closest(values, y)))
	real = list(dict.fromkeys(real))
	def error_func(a: tuple) -> float:
		return abs(ratio - a[0]/a[1]) / ratio
	real.sort(key=error_func)
	return real[:n]

if __name__ == "__main__":
	if len(argv) == 2:
		ratio     = float(argv[1])
		closest_n = closest_divider(defaults, ratio)
		print("Closest divider to {}:".format(ratio))
		
	elif len(argv) == 3:
		ratio     = float(argv[1])
		n         = int(argv[2])
		closest_n = closest_divider(defaults, ratio, n)
		if n == 1:
			print("Closest divider to {}:".format(ratio))
		else:
			print("Closest {} dividers to {}:".format(n, ratio))
		
	else:
		print("Usage: divider.py ratio (n=1)")
		exit(1)
	
	
	for x, y in closest_n:
		print("  {}/{} = {} ({}% error)".format(x, y, x/y, abs(ratio-x/y)*100//ratio))
