#!/usr/bin/env python3

a = int(input('numero de a: '))
if a > 0 and a < 1000:
	a = a
	print(a)
else:
	print("fora de 0 e 1000")


b = int(input('numero de b: '))
if b > 0 and b < 1000:
	b = b
	print(b)
else:
	print("fora de 0 e 1000")

x = a * a + b * b
print(x)
