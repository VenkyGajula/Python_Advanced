print("********Queue****")
#we can create Queue object --->q = queue.Queue()
#Methods
#1.put()---->Put an item into the queue
#2.get()---> Remove and return an item from the queue.
#Types of Queues
#1.FIFO Queues
print("**FIFO***")
import queue
q=queue.Queue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
    print(q.get(),end=' ')
print("\n")
print("**LIFO***")
import queue
q=queue.LifoQueue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
    print(q.get(),end=' ')

print("\n")

print("****Priority Queue****")
q=queue.PriorityQueue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
    print(q.get(),end=' ')
