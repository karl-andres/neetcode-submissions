class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if board[r][c] != "O":
                return

            board[r][c] = "T"
            for direction in directions:
                dr, dc = direction[0], direction[1]
                dfs(r + dr, c + dc)
            return
            

        # scan border for any connecting regions
        # if region is found (connected component) on border, then it is not surrounded

        # top and bottom rows
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # left and right columns    
        for r in range(1, rows - 1):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    continue
                elif board[r][c] == "O":
                    board[r][c] = "X"
                else:
                    board[r][c] = "O"
        
