class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        check = False
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(row, col, grid, string):
            if len(string) == 0:
                return True
            
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != string[0]:
                return False
            
            ranges = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            
            grid[row][col] = '#'
            check = False
            for way in ranges:
                check = check or dfs(row + way[0], col + way[1], grid, string[1:])
            
            grid[row][col] = string[0]
            
            return check
            
        flag = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    flag = flag or dfs(i, j, board, word)
        
        return flag