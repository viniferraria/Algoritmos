#!/usr/bin/env python3
import math

def adiantada(fx, x, h):
	# resultado = 1/(2*h)  * (-3*fx[round(x, 1)] + 4*fx[round(x+h, 1)] - fx[round(x+2*h, 1)])
	resultado = 1/(2*h) * (-3 * fx(x) + 4 * fx(x+h) - fx(x+2*h))
	return resultado

def central(fx, x, h):
	resultado = 1/(2*h) * (fx(x+h) - fx(x-h))
	return resultado

def atrasada(fx, x, h):
	resultado = 1/(2*h) * (fx(x-2*h) - 4 * fx(x+h) + 3 * fx(x))
	return resultado


def fx(x):
	return f"\n f({x}) ln = {x**2 * math.log2(x) + 1}"

def fx10(x):
	return f" f({x}) log10 = {x**2 * math.log10(x) + 1}\n"

def ffx(x):
	return f" f'({x}) ln = {2*x*math.log2(x) + x}"

def ffx10(x):
	return f" f'({x}) log10 = {2*x*math.log10(x) + x}\n"


logs = [fx, fx10, ffx, ffx10]

for i in logs:
	print(i(0.998))

# for i in logs:
# 	print(i(0.999))