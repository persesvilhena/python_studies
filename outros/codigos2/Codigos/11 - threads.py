import thread
import time

def t1(a,b,c):
   t1id = thread.get_ident()
   for i in range(100):
      time.sleep(0.1)
      print 'primeira '      
      #print t1id, i, i+a+b+c

def t2(a,b,c):
   t2id = thread.get_ident()
   for i in range(100):
      time.sleep(0.2)
      print 'segunda '
      #print t2id, i, i+a+b+c

def t3(a,b,c):
   t3id = thread.get_ident()
   for i in range(100):
      time.sleep(0.05)
      print 'terceira '
      #print t3id, i, i+a+b+c
      

thread.start_new_thread(t1, (1,2,3))
var_lock = thread.allocate_lock()
var_lock.acquire()
var_lock.release()

thread.start_new_thread(t2, (1,2,3))
var_lock2 = thread.allocate_lock()
var_lock2.acquire()
var_lock2.release()

thread.start_new_thread(t3, (1,2,3))
var_lock3 = thread.allocate_lock()
var_lock3.acquire()
var_lock3.release()
