class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[temperature, index]

        # run through loop
        for i, t in enumerate(temperatures):
            # if there is a greater temp found
            # continously pop the stack and add
            # result to result array
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res