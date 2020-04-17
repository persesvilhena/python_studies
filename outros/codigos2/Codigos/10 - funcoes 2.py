def teste(a,b=0,*c):
   print a,b,c

teste(1)

teste(1,2)

teste(1,2,3)

teste(1,2,3,4)

teste(1,2,3,4,5)

def teste(**d):
   print d


teste()

teste(a=1,b=2)

print

print dir(__builtins__)
