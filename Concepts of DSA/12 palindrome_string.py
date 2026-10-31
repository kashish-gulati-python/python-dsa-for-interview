s = "ABVVGGVVBA"
n = len(s)
left = 0
right = n-1

# def check_palindrome(st):
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# # TC O(N/2) ~ O(N)
# # SC O(1)

def check_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return check_palindrome(s, left+1, right-1)

# TC O(N/2) ~ O(N)
# SC O(N/2) -> Stack Space
    

print(check_palindrome(s, left, right))