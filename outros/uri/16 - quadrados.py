n=1
while n!=0:
    n=int(input())
    x=0
    z=n
    for i in range(n):
        x=x+(z*z)
        z=z-1
    if n!=0:
        print x
    
    
