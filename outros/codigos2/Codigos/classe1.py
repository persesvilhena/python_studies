class A:
   atributo1 = 'atributo1 da classe A'
   atributo2 = 'atributo2 da classe A'
   
def __init__(self, val_ini=1):
   "Construtor da classe A"
   self.atributo_de_instacia = val_ini

def metodo(self):
   print self.atributo_de_instacia
   print A.atributo1
