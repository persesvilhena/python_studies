arq = open('teste.txt', 'r')
for linha in arq.readlines():
   print '*'+linha+'*'
arq.close()
