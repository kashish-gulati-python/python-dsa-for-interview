num = 123455555
count = 0

while num > 0:
    count += 1
    num = num // 10

print(count)

## TC -> O(log n)
## SC -> O(1)