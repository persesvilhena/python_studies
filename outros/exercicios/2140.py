a = 1
b = 1
x = 0
y = 0
while((a != 0) and (b != 0)):
	a,b = map(int,raw_input().split())
	x = 0
	y = 0
	if((a != 0) and (b != 0)):
		troco = b - a

		if((troco >= 100) and (x == 0)):
			troco = troco - 100
			x = 1
		if((troco >= 50) and (x == 0)):
			troco = troco - 50
			x = 1
		if((troco >= 20) and (x == 0)):
			troco = troco - 20
			x = 1
		if((troco >= 10) and (x == 0)):
			troco = troco - 10
			x = 1
		if((troco >= 5) and (x == 0)):
			troco = troco - 5
			x = 1
		if((troco >= 2) and (x == 0)):
			troco = troco - 2
			x = 1



		if((troco >= 100) and (y == 0)):
			troco = troco - 100
			y = 1
		if((troco >= 50) and (y == 0)):
			troco = troco - 50
			y = 1
		if((troco >= 20) and (y == 0)):
			troco = troco - 20
			y = 1
		if((troco >= 10) and (y == 0)):
			troco = troco - 10
			y = 1
		if((troco >= 5) and (y == 0)):
			troco = troco - 5
			y = 1
		if((troco >= 2) and (y == 0)):
			troco = troco - 2
			y = 1

		if((troco == 0) and (x == 1) and (y == 1)):
			print('possible')
		else:
			print('impossible')
