class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize 0 grid
        grid = [[0] * n for i in range(m)]

        # intialize the base cases
        for i in range(n):
            grid[0][i] = 1
        
        for i in range(m):
            grid[i][0] = 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[m - 1][n - 1]