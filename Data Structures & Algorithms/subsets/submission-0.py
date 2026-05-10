"""
function backtracking(state):
    if state is a solution:
        return state
    
    for choice in all possible choices:
        if choice is valid:
            make choice
            result = backtracking(state with choice)
            if result is not failure:
                return result
            undo choice
    return failure

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # dont include nums[i]
            subset.pop()
            dfs(i + 1)

        
        dfs(0)
        return res