num_str = ["3", "6", "2", "1"]
low_str = ["kashish", "is", "dope"]

result_int = map(int, num_str)
result_upper = map(str.upper, low_str)

print(list(result_int))
print(list(result_upper))