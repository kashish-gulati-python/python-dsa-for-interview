"""
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

from typing import List

# linear traversal + membership checking
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = []

        for i in range(len(nums)):
            if nums[i] in L: # dup is a list, so membership checking takes O(n) in the worst case
                continue
            else:
                L.append(nums[i])

        nums[:] = L

        return len(L)
# Time Complexity: O(n²)
# Space Complexity: O(n)
# You could replace dup with a set to improve lookup time to O(1) average, but you'd still use O(n) extra space.


# Two Pointers
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in range(i+1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                
        return i+1
# Time: O(n) — one traversal.
# Space: O(1) — no additional data structure proportional to input size

# Two Pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write += 1

        return write
# Time: O(n) — one traversal.
# Space: O(1) — no additional data structure proportional to input size



"""
Problem characteristic	Think about
Sorted array + duplicates	Two pointers
Sorted array + pair sum	Two pointers
Need fast membership lookup	Hash set
Need key-value lookup	Dictionary
Nested brackets	Stack
Sorted array + search	Binary search
"""