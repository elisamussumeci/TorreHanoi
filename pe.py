a =5
b =1
c = 16

n=32

seed = 10

def function(xo,):
	for i in range(n):
		x = a * xo +b;
		y = x%c;
		xo = y
	return x
