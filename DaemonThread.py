print("*****Daemon thread****")
#set the daemon thread Nature
#t.setDaemon(true)
from threading import *
print(current_thread().isDaemon())
#print(current_thread().setDaemon(True))
#dcefault Nature
from threading import *
def job():
    print("Child Thread")
t=Thread(target=job)
print(t.isDaemon())#False
t.setDaemon(True)
print(t.isDaemon()) #True

print("***********")
import time
def job():
    for i in range(10):
        print("Lazy Thread")
        time.sleep(2)
t=Thread(target=job)
#t.setDaemon(True)===>Line-1
t.start()
time.sleep(5)
print("End Of Main Thread")

print("*****Synchronization*****")
#if multiple threads are executing simultaneously then there may be change of data inconsistency problems
def wish(name):
    for i in range(10):
        print("Good Evening:",end='')
        time.sleep(2)
        print(name)
t1=Thread(target=wish,args=("venky",)) 
t2=Thread(target=wish,args=("Hari",))
t1.start()
t2.start()
