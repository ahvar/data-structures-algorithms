class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "{": "}",
            "]": "[",
        }
        stack = []
        for c in s:
            if c in brackets.keys():
                stack.append(c)
                continue

            if not stack or stack[-1] != brackets.get(c):
                return False

            stack.pop()
        return not stack
