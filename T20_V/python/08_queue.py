
# a queue also removes the value when you read it

import queue

q = queue.Queue()

q.put("hello1")
q.put("hello2")

item1 = q.get()
item2 = q.get()

print(item1)
print(item2)
print("Queue is now empty")