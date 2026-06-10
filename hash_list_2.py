"""
Constraints:
1 <= n[i] <= 10
n, m can have 10^8 elements
"""
n = [1, 3, 6, 2, 5, 2, 7, 1, 5, 9, 3]
m = [3, 4, 1, 29, 550, 2]

hash_list = [0]*11

for i in n:
    hash_list[i] += 1

for i in m:
    if i >= 10 or i <= 0:
        print(f"{i}:", 0)
    else:
        print(f"{i}:", hash_list[i])

## TC -> O(n) * O(m)
## SC -> O(11) ~ O(1)