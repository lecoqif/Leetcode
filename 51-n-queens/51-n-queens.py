class Solution:
    def __init__(self) -> None:
        self.rows = []
        self.cols = []
        self.diagonals = []
        self.antidiagonals = []
        self.ret = []
        self.n = 0
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.rows = [False for _ in range(n)]
        self.cols = [False for _ in range(n)]
        self.n = n
        
        self.diagonals = [False for _ in range(2 * n - 1)]
        self.antidiagonals = [False for _ in range(2 * n - 1)]
        
        self.backtrack(0, [])
    
        return self.ret
    
    def backtrack(self, currRow, output) -> None:
        if currRow == self.n:
            self.ret.append(output[:])
            return
        
        for i in range(self.n):
            if self.checkValidPlacement(currRow, i):
                self.toggleQueen(currRow, i, True)
                output.append("." * (i - 0) + "Q" + "." * (self.n - 1 - i))
                self.backtrack(currRow + 1, output)
                output.pop()
                self.toggleQueen(currRow, i, False)
            
    
    def checkValidPlacement(self, row, col):
        if self.rows[row] or self.cols[col] or self.diagonals[row + col] or self.antidiagonals[row - col + self.n - 1]:
            return False
        
        return True
    
    def toggleQueen(self, row, col, boolVal) -> bool:
        self.rows[row] = boolVal
        self.cols[col] = boolVal
        self.diagonals[row + col] = boolVal
        self.antidiagonals[row - col + self.n - 1] = boolVal
    

        
        
        
        
        