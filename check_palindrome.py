num = 1234
result = 0
n = num

while n > 0:
    last_digit = n % 10
    result = result*10 + last_digit
    n = n // 10

print(result == num)

## TC -> O(log n)
## SC -> O(1)