from queue import Queue

# Create a queue and add items
q = Queue()
q.put("Apple")
q.put("Banana")
q.put("Cherry")
print(q.get())

q2 = Queue()
q2.put("Item 1")
q2.put("Item 2")

if not q2.empty():
    print(q2.get())
