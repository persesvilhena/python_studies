i = int(raw_input())


for item in range(i):

	entrada = raw_input() 
	numerosComoString = entrada.split(" ")
	numeros = [int(numero) for numero in numerosComoString] 
	hr, mints, porta = numeros
	if porta==1:
		print "%02d:%02d - A porta abriu!" % (hr,mints)
	elif porta==0:
		print "%02d:%02d - A porta fechou!" % (hr,mints)


