num = 153
l = len(str(num))
result = 0
n = num

while n > 0:
    last_digit = n % 10
    result = result + last_digit**l
    n = n // 10

print(result == num)

## TC -> O(log n)
## SC -> O(1)