"""
Constraints:
n and m can have small case English albhabets
n can have 26 characters
m can have 26 characters
"""

# ord(a) = 97, ord(z) = 126
s = ['a', 'f', 'r', 'r', 'a', 'c', 'a', 'f', 'h', 'z', 'b', 'r']
c = ['d', 'l', 'a', 'q', 'z', 'f']

# # Method 1:
# hash_list = [0]*127 # space wasted

# for char in s:
#     hash_list[ord(char)] += 1

# for char in c:
#     print(char, hash_list[ord(char)])

# Method 2:
hash_list = [0]*26

for char in s:
    index = ord(char) - 97
    hash_list[index] += 1

for char in c:
    index = ord(char) - 97
    print(char, hash_list[index])