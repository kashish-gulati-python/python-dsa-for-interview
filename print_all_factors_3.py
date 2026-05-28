from math import sqrt

num = 36
result = []

for i in range(1, int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if num // i != i:
            result.append(num//i)
        # result.sort() # O(nlogn)

print(result)

## TC -> O(n**0.5) ~ O(n)
## SC -> O(k)