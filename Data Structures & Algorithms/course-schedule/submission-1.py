class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj list
        adj_list = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        # create sets
        call_stack = set()
        
        def dfs(crs):
            if crs in call_stack:
                # cycle detected
                return False
            # if we've reached the end
            if adj_list[crs] == []:
                return True
            
            call_stack.add(crs)

            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False

            call_stack.remove(crs)
            return True
        
        # main loop
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True