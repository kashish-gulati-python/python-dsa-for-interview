from collections import Counter

data = ["apple", "banana", "apple", "orange"]

c = Counter(data)

print(c)
print(c["banana"])
print(c.most_common(2))
print(Counter("kashish"))
print(c.keys())
print(c.values())

for i in c:
    print(i)