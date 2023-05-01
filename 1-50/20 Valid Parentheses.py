class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for ch in s:
            if ch in dict:
                stack.append(ch)
            elif not len(stack) or ch != dict[stack.pop()]:
                return False
        return len(stack) == 0