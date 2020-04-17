entrada = raw_input() 
numerosComoString = entrada.split(" ")
numeros = [int(numero) for numero in numerosComoString] 
a, b, c = numeros

if (a==b or a==c or b==c) or ((a+b==c) or (b+c==a) or (a+c==b)):
	print 'S'
else:
	print'N'
