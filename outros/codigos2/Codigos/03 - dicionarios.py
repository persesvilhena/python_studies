estoque = {'peras': 5, 'laranjas': 2}

print estoque['peras']

estoque['peras'] = 4

print estoque['peras']

estoque['macas'] = 2

print estoque

estoque.get('peras','nao temos')

estoque.get('melao','nao temos')

print estoque.has_key('uvas')

print estoque.items()

def imprime_frutas():
   for fruta, qtd in estoque.items():
      print 'Fruta: %s - %s' % (fruta, qtd)

imprime_frutas()





