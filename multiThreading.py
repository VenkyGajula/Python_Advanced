print("************multiThreading*********")
import threading
print('current executing Thread :',threading.current_thread().getName())

print("******** Creating a Thread without using any class**********")
from threading import *
def display():
 for i in range(1,11):
    print("Child Thread")
t=Thread(target=display) #creating Thread object
t.start() #starting of Thread
for i in range(1,11):
    print("Main Thread")

print("******** Creating a Thread by extending Thread class **********")
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread-1")
t=MyThread()
t.start()
for i in range(10):
    print("Main Thread-1")

print("******** Creating a Thread without extending Thread class **********")
class Test:
    def display(self):
        for i in range(10):
            print("Child Thread-2")
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread-2")

print("*****Without multi threading*******")
from threading import *
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:",2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:",n*n)
numbers=[1,2,3,4,5,6]
begintime=time.time()
doubles(numbers)
squares(numbers)
print("The total time taken:",time.time()-begintime)

print("*****With multithreading:*******")
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:",2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:",n*n)
numbers=[1,2,3,4,5,6]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("The total time taken:",time.time()-begintime)
from threading import*
print("*****Setting and Getting Name of a Thread*********")
print('current executing Thread :',threading.current_thread().getName())
current_thread().setName("venky Gajula")
print(current_thread().getName())
print(current_thread().name)
