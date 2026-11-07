"""
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


# Python slicing
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # O(n)
        rev_text = cleaned_text[::-1]
        return cleaned_text == rev_text
# TC: O(n)
# SC: O(m)

import re

# Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # O(n)
        n = len(cleaned_text)
        if n == 0:
            return True
        left = 0
        right = n-1
        while left <= right: # O(m)
            if cleaned_text[left] != cleaned_text[right]:
                return False
            left += 1
            right -= 1
        return True
# TC: O(n)
# SC: O(m)

# Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
# Time: O(n)
# Auxiliary space: O(1)