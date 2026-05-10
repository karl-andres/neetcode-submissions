class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0

        for c in s:
            if c.isdigit():
                # build multi-digit number
                num = num * 10 + int(c)

            elif c == '[':
                stack.append(num)
                stack.append(c)
                num = 0

            elif c == ']':
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()              # remove '['
                k = stack.pop()          # number before '['
                stack.append(substr * k)

            else:
                stack.append(c)

        return "".join(stack)
