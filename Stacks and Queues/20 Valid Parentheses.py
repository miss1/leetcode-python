class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if len(stack) == 0 or c not in mapping:
                stack.append(c)
            elif mapping[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
