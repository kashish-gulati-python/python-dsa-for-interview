n = [1, 3, 6, 2, 5, 2, 7, 1, 5, 9, 3]
m = [3, 4, 1, 29, 550, 2]

hash_dict = {}

for i in n:
    hash_dict[n[i]] = hash_dict.get(n[i], 0) + 1

for i in m:
    if i in hash_dict:
        print(f"{i}: {hash_dict[i]}")
    else:
        print(f"{i}: 0")

## TC -> O(n) * O(m)
## SC -> O(1)