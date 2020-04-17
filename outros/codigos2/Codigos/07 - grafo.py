grafo = {'A': ['B','C'], 'B': ['A','C','D'], 'C': ['A','B'], 'D': ['B']}

def ache_caminho(grafo, inicio, final, caminho=[]):
   caminho = caminho + [inicio]
   if inicio == final:
      return caminho
   for nodo in grafo[inicio]:
      if nodo not in caminho:
         novocaminho = ache_caminho(grafo, nodo, final, caminho)
         if novocaminho:
            return novocaminho
   return None

print ache_caminho(grafo, 'A', 'D')

print ache_caminho(grafo, 'B', 'A')

print ache_caminho(grafo, 'D', 'C')

print ache_caminho(grafo, 'A', 'A')

print ache_caminho(grafo, 'A', 'E')
