valor = (raw_input().split())
#numerosComoString = valor.split(" ")
nums = [float(num) for num in valor] 
c, p, f = nums
f = c * f
if f<=p:
	print "S"
else:
	print"N"