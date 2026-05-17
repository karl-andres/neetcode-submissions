from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols =  len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        infected = 2

        fresh = 1

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == infected:
                    queue.append((r, c))
        
        minute = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                r, c = current[0], current[1]

                # mark as visited
                grid[r][c] = 3 # 3 is our mark for being visited

                for direction in directions:
                    dr, dc = r + direction[0], c + direction[1]
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == fresh:
                        grid[dr][dc] = infected
                        queue.append((dr, dc))
            if queue:
                minute += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == fresh:
                    return -1

        return minute