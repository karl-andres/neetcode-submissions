class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        rows, cols = len(board), len(board[0])

        visiting = set()

        def search(r, c):
            print(board[r][c])
            visiting.add((r, c))
            if len(visiting) == len(word):
                return True
            
            for direc in directions:
                dr, dc = r + direc[0], c + direc[1]
                if 0 <= dr < rows and 0 <= dc < cols and board[dr][dc] == word[len(visiting)] and (dr,dc) not in visiting:
                    if search(dr, dc):
                        return True

            visiting.remove((r, c))

            return False

        for r in range(rows):
            for c in range(cols):
                letter = board[r][c]
                if letter == word[0]:
                    if search(r, c):
                        return True
        
        return False