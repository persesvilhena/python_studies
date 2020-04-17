import classe2
print classe2.A.metodo_statico()
x = classe2.A()
print x.metodo_statico()


print hasattr(x, 'metodo_statico')

#delattr(objeto, nome)
print getattr(x, 'metodo_statico')

y = getattr(x, 'metodo_statico')

print y

#setattr(objeto, nome, valor)
