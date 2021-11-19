print("******Synchronization****")
#three concepts are there
#1.lock
#2.Rlock
#3.semaphore
print("****Synchronization By using Lock concept********")
#l=lock()===> hold the one threads
#l.acquire()==>A thread can acquire the lock by using acquire() Methods
#l.release()==>A Thread can release the lock by using release() method.
from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("Good Evening:",end='')
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=("venky",))
t2=Thread(target=wish,args=("Manoj",))
t3=Thread(target=wish,args=("HAri",))
t1.start()
t2.start()
t3.start()

print("*****Demo Program for synchronization by using RLock****")
l=RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    l.release()
    return result
def results(n):
    print("The Factorial of",n,"is:",factorial(n))
t1=Thread(target=results,args=(5,))
t2=Thread(target=results,args=(9,))
t1.start()
t2.start()

print("Synchronization by using Semaphore")
import time
s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(10):
        print("Good Evening:",end='')
        time.sleep(2)
        print(name)
        s.release()
t1=Thread(target=wish,args=("Venu",))
t2=Thread(target=wish,args=("Ram",))
t3=Thread(target=wish,args=("Hari",))
t4=Thread(target=wish,args=("RAvali",))
t5=Thread(target=wish,args=("Sandy",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
