"""
xue hua piao piao bei feng xiao xiao
"""
class Solution:
    def Zeros(self, i, j, row, col, grid):
        if i < 0 or i >= row or j < 0 or j >= col:
            return
        if grid[i][j] == '0':
            return

        grid[i][j] = "0"
        self.Zeros(i + 1, j, row, col, grid)
        self.Zeros(i - 1, j, row, col, grid)
        self.Zeros(i, j + 1, row, col, grid)
        self.Zeros(i, j - 1, row, col, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    self.Zeros(i, j, row, col, grid)
    
        return count