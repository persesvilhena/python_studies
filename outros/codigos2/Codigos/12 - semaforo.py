import threading

def funcao(a,b):
   for i in range(a):
      print i   

t1 = threading.Thread(target=funcao,args=((1000,0)))
t1.start()

t2 = threading.Thread(target=funcao,args=((100,0)))
t2.start()

t3 = threading.Thread(target=funcao,args=((10,0)))
t3.start()

sem = threading.Semaphore(2)
sem.acquire()
sem.release()
