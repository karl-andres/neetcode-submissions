"""
# Topological Sort (using DFS)

Literally just:
Topological Sort == postorder DFS + reverse
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            adj_list[prereq[0]].append(prereq[1])
        
        call_stack = set()
        visited = set()
        res = []
        def dfs(node):
            if node in call_stack:
                return False
            if node in visited:
                return True
            
            call_stack.add(node)

            for neigh in adj_list[node]:
                if not dfs(neigh):
                    return False
            
            call_stack.remove(node)
            visited.add(node)

            res.append(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return []
        return res