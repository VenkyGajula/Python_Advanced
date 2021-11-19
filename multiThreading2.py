print("****Thread Identification Number (ident)*****")
from threading import *
def test():
    print("Child Thread")
t=Thread(target=test)
t.start()
print("Main Thread Identification Number:",current_thread().ident)
print("Child Thread Identification Number:",t.ident)

print("****active_count()*****")
import time
def display():
    print(current_thread().getName(),"...started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")
print("The Number of active Threads:",active_count())
t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t3=Thread(target=display,name="ChildThread3")
t1.start()
t2.start()
t3.start()
print("The Number of active Threads:",active_count())
time.sleep(5)
print("The Number of active Threads:",active_count())

print("****enumerate()*****")
def display():
    print(current_thread().getName(),"...started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")
t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t3=Thread(target=display,name="ChildThread3")
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
    print("Thread Name:",t.name)
time.sleep(5)
l=enumerate()
for t in l:
    print("Thread Name:",t.name)

print("*******isAlive()*******")
import time
def display():
    print(current_thread().getName(),"...started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")
t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t1.start()
t2.start()
print(t1.name,"is Alive :",t1.isAlive())
print(t2.name,"is Alive :",t2.isAlive())
time.sleep(5)
print(t1.name,"is Alive :",t1.isAlive())
print(t2.name,"is Alive :",t2.isAlive())

print("*****join()*****")
def display():
    for i in range(10):
        print("venky Thread")
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join()#This Line executed by Main Thread
for i in range(10):
    print("venu Thread")
