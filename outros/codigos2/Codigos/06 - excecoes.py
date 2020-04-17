try:
   arq=open('teste4.txt','r')
   print arq.readlines()
   arq.close()
except:
   print 'Erro lendo arquivo teste4.txt'


numero = 5

#if numero < 10:
#   raise 'Numero menor que zero'

EXCECAO_NUM = "Numero menor que zero"
def verifica(numero):
   if numero < 10:
      raise EXCECAO_NUM
    
try:
   verifica(numero)
except EXCECAO_NUM:
   print "Digite um numero >= que 10!"
except:
   print "Erro ao validar numero!"


try:
   arq = open('teste4.txt', 'r')
except:
   print "Erro ao ler arquivo"
else:
   # Sera executado se qnd nao houver excecao
   print "Posso ler o arquivo"


try:
   arq = open('teste3.txt', 'r')
finally:
   # Sera executado sempre! (com ou sem excecao)
   print "Sera que posso ler o arquivo?"
   
# Podemos usar except ou finally, nunca os dois
