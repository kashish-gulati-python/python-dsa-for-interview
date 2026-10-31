"""
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
# Method 1: Brute Force
# TC = O(n²)
# SC = O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)): # O(n)
            for j in range(i + 1, len(nums)): # O(n)
                if nums[i] + nums[j] == target:
                    return [i, j]

# Method 2: Hashing
# TC = O(n)
# SC = O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
# nums = [3,2,4], target = 6
        seen = {}

        for i, num in enumerate(nums): # O(n)
            complement = target - num

            if complement in seen: # O(1) average case
                return [seen[complement], i]

            seen[num] = i # O(1) average case
# Output: [1,2]
