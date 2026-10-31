"""
Constraints:
1 <= n[i] <= 10
n can have 10^8 elements
m can have 10^8 elements
"""

n = [1, 4, 5, 2, 5, 1, 9, 4, 10]
m = [3, 1, 5, 2, 31, 20, 6]

# # Method 1: Brute Force
# # TC O(M*N) ~ O(N^2)
# # SC O(1)
# for num in m: # O(M)
#     count = 0
#     for x in n: # O(N)
#         if x == num:
#             count += 1
#     print(num, count)

# # Method 2: Hashing
# # TC O(M+N) ~ O(N)
# # SC O(11) ~ O(1)
# hash_list = [0] * 11
# for num in n: # O(N)
#     hash_list[num] += 1

# for num in m: # O(M)
#     if num<1 or num>10:
#         print(num, 0)
#     else:
#         print(num, hash_list[num])

# Method 3: Dict mapping
# TC O(M*N) ~ O(N^2)
# SC O(1)
d = dict()
for i in range(len(n)): # O(N)
    d[n[i]] = d.get(n[i], 0) + 1

for num in m:
    print(num, d.get(num,0))