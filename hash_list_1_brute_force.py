"""
Constraints:
1 <= n[i] <= 10
n, m can have 10^8 elements
"""
n = [1, 3, 6, 2, 5, 2, 7, 1, 5, 9, 3]
m = [3, 4, 1, 29, 550, 2]

for i in m:
    count = 0
    for j in n:
        if i == j:
            count += 1
    print(f"{i}:", count)

## TC -> O(n^2)
## SC -> O(1)