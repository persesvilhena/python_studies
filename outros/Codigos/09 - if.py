n = int(raw_input('digite um numero: '))

if ((n%2)==0):
   print str(n) + ' e par!'
else:
   print str(n) + ' e impar!'

if (n>10):
   print str(n) + ' e maior que 10!'
elif (n<10):
   print str(n) + ' e menor que 10!'
else:
   print str(n) + ' e igual a 10!'

temp = int(raw_input('Entre com a temperatura: '))
if temp < 0:
   print 'Quente...'
elif 0 <= temp <= 20:
   print 'Muito quente'
elif 21 <= temp <= 25:
   print 'Quente pra porra'
elif 26 <= temp <= 35:
   print 'Bahia'
else:
   print 'Inferno!'   
