"b before a"
"must be acyclic"
"during call stack, u mustn't have duplicates"
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj list
        adj_list = {}
        for prereq in prerequisites:
            if prereq[0] not in adj_list:
                adj_list[prereq[0]] = [prereq[1]]
            else:
                adj_list[prereq[0]].append(prereq[1])
        
        # create sets
        call_stack = set()
        visited = set()

        def dfs(node):
            if node in call_stack:
                return False
            if node in visited:
                return True

            call_stack.add(node)

            for neigh in adj_list.get(node, []):
                if not dfs(neigh):
                    return False
            
            call_stack.remove(node)
            visited.add(node)

            return True
            
        for node in adj_list:
            if node not in visited:
                if not dfs(node):
                    return False

        return True