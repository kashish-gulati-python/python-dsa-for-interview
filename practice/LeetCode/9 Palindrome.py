# Time: O(log x)
# Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        result = 0

        while num > 0:
            ld = num % 10
            result = (result * 10) + ld
            num = num // 10

        return x == result

# Time: O(log x)
# Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10