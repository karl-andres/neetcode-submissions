class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for edge in edges:
            u, v = edge[0], edge[1]
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        def dfs(u):
            visited.add(u)
            for v in adj_list[u]:
                if v not in visited:
                    dfs(v)
        
        for u in adj_list:
            # found component
            if u not in visited:
                res += 1
                dfs(u)
        
        return res