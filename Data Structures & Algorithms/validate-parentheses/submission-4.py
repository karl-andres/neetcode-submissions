class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")":"(", "}":"{","]":"["}

        for b in s:
            if b == "[" or b == "{" or b == "(":
                stack.append(b)
            else:
                if stack and close_to_open[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False