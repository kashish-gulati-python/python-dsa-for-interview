num = 20
result = []
n = num

while n > 0:
    result.append(n)
    n = n // 2

print(result)

## TC -> O(log2n)
## SC -> O(k)