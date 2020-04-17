entrada = raw_input() 
numerosComoString = entrada.split(" ")
numeros = [int(numero) for numero in numerosComoString] 
a, b, c = numeros

if (a+b)>c and (a+c)>b and (b+c)>a:
	if a==b and b==c and a==c:
		print 'Valido-Equilatero'
	elif a!=b and b!=c and a!=c:
		print 'Valido-Escaleno'
	elif a==b or b==c or a==c:
		print 'Valido-Isoceles'
	if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2):
            print 'Retangulo: S'
        else:
            print 'Retangulo: N'
else:
	print 'Invalido'
		