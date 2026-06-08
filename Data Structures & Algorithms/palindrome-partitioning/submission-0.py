class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []
        def dfs(i):
            if i == len(s):
                res.append(partition.copy())
                return

            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if substring[::-1] == substring:
                    partition.append(substring)
                    dfs(j + 1)
                    partition.pop()
        dfs(0)
        return res