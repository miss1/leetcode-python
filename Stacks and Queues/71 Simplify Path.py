class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split('/')
        for p in arr:
            if p == '' or p == '.':
                continue
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
