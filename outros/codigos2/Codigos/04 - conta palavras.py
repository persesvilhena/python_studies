palavra_count = {}

arqnom = raw_input('Digite o nome do Arquivo: ')

arq = open(arqnom, 'r')

for linha in arq.readlines():
   palavras = linha.split()
   for palavra in palavras:
      palavra_count[palavra] = palavra_count.get(palavra,0) + 1

arq.close()

palavras = palavra_count.keys()
palavras.sort()
for palavra in palavras:
   print 'Palavra: %s, Quantidade: %05i' % (palavra, palavra_count[palavra])
