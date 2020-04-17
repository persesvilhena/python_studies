n=1
m=1
while n!=0 and m!=0:
	entrada = raw_input() 
	numerosComoString = entrada.split(" ")
	numeros = [float(numero) for numero in numerosComoString] 
	n , m = numeros

	troco = m-n
	if n!=0 and m!=0:
		if troco!=7 and troco!=12 and troco!=22 and troco!=52 and troco!=102 and troco!=15 and troco!=25 and troco!=55 and troco!=105 and troco!=30 and troco!=60 and troco!=110 and troco!=70 and troco!=120 and troco!=150:
			print 'impossible'
		else:
			print 'possible'
    