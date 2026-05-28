num = 12345

while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

## TC -> O(log n)
## SC -> O(1)