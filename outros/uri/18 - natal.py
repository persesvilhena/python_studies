import datetime
while True:
    try:
		natal = datetime.date(day=25, month=12, year=2016)

		entrada = raw_input() 
		numerosComoString = entrada.split(" ")
		numeros = [int(numero) for numero in numerosComoString] 
		mes , dia = numeros

		data = datetime.date(day= dia, month= mes, year=2016)

		data-natal
		datetime.timedelta(123)

		diferenca = natal-data

		if diferenca.days==0:
			print "E natal!"
		elif diferenca.days==1:
			print "E vespera de natal!"
		elif diferenca.days<0:
			print "Ja passou!"
		else:
			print ('Faltam %d dias para o natal!'%(diferenca.days))

    except: break