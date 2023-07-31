class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) == 0 or stack[-1] == c or (stack[-1] != c.lower() and stack[-1] != c.upper()):
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)
