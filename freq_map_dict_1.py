nums = [1, 3, 6, 2, 5, 2, 7, 1, 5, 9, 3]

freq_map = {}
for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)

## TC -> O(n)
## SC -> O(n)