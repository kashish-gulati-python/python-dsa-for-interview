num = 19
result = []

for x in range(1, num//2):
    if num % x == 0:
        result.append(x)
result.append(num)

print(result)

## TC -> O(n/2) ~ O(n)
## SC -> O(k)