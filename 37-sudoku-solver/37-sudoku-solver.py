class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]
        q = []
        
        ROWS, COLS = len(board), len(board[0])
    
        def setVal(row: int, col: int, val: int) -> None:
            rows[row].add(int(val))
            cols[col].add(int(val))
            sub_boxes[(row // 3) * 3 + (col // 3)].add(int(val))
            
        def unsetVal(row: int, col: int, val: int) -> None:
            rows[row].remove(int(val))
            cols[col].remove(int(val))
            sub_boxes[(row // 3) * 3 + (col // 3)].remove(int(val))
            
        def checkVal(row: int, col: int, val: int) -> bool:
            if val in rows[row] or val in cols[col] or val in sub_boxes[(row // 3) * 3 + (col // 3)]:
                return False
            
            return True
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != '.':
                    setVal(i, j, board[i][j])
                else:
                    q.append((i, j))
        
        def backtrack(idx = 0) -> bool:
            if idx == len(q):
                return True
            
            r, c = q[idx]
            
            for i in range(1, 10):
                if not checkVal(r, c, i):
                    continue
                
                board[r][c] = str(i)
                setVal(r, c, i)
                
                if backtrack(idx + 1):
                    return True
                
                board[r][c] = '.'
                unsetVal(r, c, i)

        backtrack()
        return board
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        