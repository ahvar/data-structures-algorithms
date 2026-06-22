class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {"}": "{", ")": "(", "]": "["}
        stack = []
        for c in s:
            if c in "[{(":
                stack.append(c)
                continue
            if not stack or stack[-1] != paren_dict.get(c):
                return False
        return True
