class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                val2 = stack.pop()
                val1 = stack.pop()
                new_val = int(val1) + int(val2)
                stack.append(new_val)
            elif token == '-':
                val2 = stack.pop()
                val1 = stack.pop()
                new_val = int(val1) - int(val2)
                stack.append(new_val)
            elif token == '*':
                val2 = stack.pop()
                val1 = stack.pop()
                new_val = int(val1) * int(val2)
                stack.append(new_val)
            elif token == '/':
                val2 = stack.pop()
                val1 = stack.pop()
                new_val = int(int(val1) / int(val2))
                stack.append(new_val)
            else:
                stack.append(int(token))
        return stack[0]