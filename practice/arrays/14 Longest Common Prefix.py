class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
# Input: strs = ["flower","flow","flight"]
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                
        return prefix
# Output: "fl"
    

"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""