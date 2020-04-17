cont=0
while True:
    cont+=1
    try:
        N=int(input())
        st=[0]
        n=1
        
        for i in range(N+1):
            for k2 in range(i):
                st.append(i)
                n+=1
        if n==1:
            print('Caso %d: %d numero'%(cont,n))
        else:
            print('Caso %d: %d numeros'%(cont,n))

        for i in range(len(st)-1):
             print(st[i]),
        print(st[len(st)-1])
        print
    except: break