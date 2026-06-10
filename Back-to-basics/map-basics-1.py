def double(n):
    return n*2

numbers = [1, 4, 2, 8]

result = map(double, numbers)
# result = map(lambda n: n*2, numbers)

print(list(result))