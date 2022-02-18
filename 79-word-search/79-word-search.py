class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.ROWS = len(board)
        self.COLS = len(board[0])
        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if board[i][j] == word[0] and self.dfs(i, j, 0):
                    return True
        
        return False
    
    def dfs(self, row: int, col: int, idx: int) -> bool:
        if idx == len(self.word):
            return True
        
        if not (0 <= row < self.ROWS and 0 <= col < self.COLS and idx < len(self.word) and self.board[row][col] == self.word[idx]):
            return False
        
        ranges = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        self.board[row][col] = '#'
        
        ret = False
        
        for way in ranges:
            ret |= self.dfs(row + way[0], col + way[1], idx + 1)
        
        self.board[row][col] = self.word[idx]
        
        return ret
                    
        