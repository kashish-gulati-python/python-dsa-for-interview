from collections import deque

# 1. Initialization
# You can create an empty deque or initialize it with an iterable
d = deque(['b', 'c', 'd'])
print(d)

# 2. Adding elements
d.append('e')          # Adds to the right (end) -> deque(['b', 'c', 'd', 'e'])
print(d)
d.appendleft('a')      # Adds to the left (front) -> deque(['a', 'b', 'c', 'd', 'e'])
print(d)

# 3. Removing elements
d.pop()                # Removes and returns from the right -> returns 'e'
print(d)
d.popleft()            # Removes and returns from the left -> returns 'a'
print(d)

# Current state: deque(['b', 'c', 'd'])

d.rotate(1)  # deque(['d', 'b', 'c'])
print(d)

# Only keeps the last 3 items
history = deque(maxlen=3)
history.append(1)
history.append(2)
history.append(3)
history.append(4)  # 1 gets pushed out!
print(history)
# history is now: deque([2, 3, 4], maxlen=3)