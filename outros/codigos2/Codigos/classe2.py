class A:
   atributo = 'atributo da classe'
   
   def metodo_statico():
      print A.atributo

   metodo_statico = staticmethod(metodo_statico)


