class Solution:
    def countIsland(self, r, c, rows, cols, grid, area):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if grid[r][c] == 0:
            return 0
        
        grid[r][c] = 0
        return 1 + self.countIsland(r + 1, c, rows, cols, grid, area) + self.countIsland(r - 1, c, rows, cols, grid, area) + self.countIsland(r, c + 1, rows, cols, grid, area) + self.countIsland(r, c - 1, rows, cols, grid, area)
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.countIsland(r, c, rows, cols, grid, 0))

        return max_area