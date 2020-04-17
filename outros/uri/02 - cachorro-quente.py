entrada = raw_input() 
numerosComoString = entrada.split(" ")
numeros = [float(numero) for numero in numerosComoString] 
h , p = numeros
print "%.2f" % (h/p)
