n = int(raw_input())
entrada = raw_input() 
numerosComoString = entrada.split(" ")
numeros = [int(numero) for numero in numerosComoString] 
a, l, p = numeros

if a>=n and l>=n and p>=n:
	print "S"
else:
	print"N"

