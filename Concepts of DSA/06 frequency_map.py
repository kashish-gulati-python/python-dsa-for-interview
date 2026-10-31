nums = [4, 2, 9, 22, 17, 4, 1, 2 ,5, 2, 9, 1, 77]

# # Method 1
# # TC O(n)
# # SC O(n)
# freq_map = dict()
# for i in range(0, len(nums)): # O(n)
#     if nums[i] in freq_map: # O(1)
#         freq_map[nums[i]] += 1 # O(1)
#     else:
#         freq_map[nums[i]] = 1 # O(1)

# print(freq_map)

# Method 2
# TC O(n)
# SC O(n)
hash_map = dict()
for i in range(0, len(nums)): # O(n)
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

print(hash_map)