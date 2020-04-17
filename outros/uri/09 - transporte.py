entrada = raw_input() 
numerosComoString = entrada.split(" ")
conteineres = [int(numero) for numero in numerosComoString] 
a, b, c = conteineres

entrada = raw_input() 
numerosComoString = entrada.split(" ")
navio = [int(numero) for numero in numerosComoString] 
x, y, z = navio

print ((x/a)*(y/b)*(z/c))