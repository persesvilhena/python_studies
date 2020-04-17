entrada = raw_input() 
numerosComoString = entrada.split(" ")
numeros = [int(numero) for numero in numerosComoString] 
c, n = numeros

print c % n