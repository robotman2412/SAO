#!/usr/bin/env python3

import sys
from sys import argv
from divider import *

# r2 = 0.6 / (v - 0.6) * r1
# r2 * (v - 0.6) = 0.6 * r1
# v - 0.6 = 0.6 * r1 / r2
# v = 0.6 * r1 / r2 + 0.6

# v = 0.6 * x + 0.6
# 0.6 * x = v - 0.6
# x = v / 0.6 - 1

if __name__ == "__main__":
	if len(argv) == 2:
		voltage   = float(argv[1])
		ratio     = voltage/0.6 - 1
		closest_n = closest_divider(defaults, ratio)
		print("Ratio for {}V: {}".format(voltage, ratio))
		print("Closest divider to {}:".format(ratio))
		
	elif len(argv) == 3:
		voltage   = float(argv[1])
		n         = int(argv[2])
		ratio     = voltage/0.6 - 1
		closest_n = closest_divider(defaults, ratio, n)
		print("Ratio for {}V: {}".format(voltage, ratio))
		if n == 1:
			print("Closest divider to {}:".format(ratio))
		else:
			print("Closest {} dividers to {}:".format(n, ratio))
		
	else:
		print("Usage: sy8079_calc.py voltage [n=1]")
		sys.exit(1)
	
	for x, y in closest_n:
		v = 0.6 + 0.6*x/y
		print("  {}/{} yields {}V ({}% error)".format(x, y, v, abs(voltage-v)*100//voltage))
