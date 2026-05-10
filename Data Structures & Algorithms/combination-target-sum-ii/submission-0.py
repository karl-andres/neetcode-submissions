class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        seen = []

        candidates.sort()

        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or sum(subset) > target:
                return

            # check all combinations that include element at index i
            subset.append(candidates[i])
            dfs(i + 1)

            # check all combinations that do not include element at index i
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res