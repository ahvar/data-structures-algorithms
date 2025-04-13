from collections import deque

# Create a deque and add items
d = deque()
d.append("Middle")
d.append("Right end")
d.appendleft("Left end")

print(d.pop())  # pop it off the "Right end"
print(d.popleft())  # pop it off the "Left end"

d2 = deque(["Apple", "Banana", "Cherry"])
d2.rotate(1)
print(d2)
