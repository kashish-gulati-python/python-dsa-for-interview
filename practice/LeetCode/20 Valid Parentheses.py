class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' or c == ']' or c == '}':
                if stack == []:
                    return False
                popped = stack.pop()
                if popped == '(' and c != ')':
                    return False
                if popped == '[' and c != ']':
                    return False
                if popped == '{' and c != '}':
                    return False
        if stack == []:
            return True
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}':
                if stack == []:
                    return False
                popped = stack.pop()
                if popped == '(' and c != ')':
                    return False
                if popped == '[' and c != ']':
                    return False
                if popped == '{' and c != '}':
                    return False
        if stack == []:
            return True
        return False

            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in pairs:
                if not stack or pairs[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack
