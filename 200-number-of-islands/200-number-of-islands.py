class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(row: int, col: int):
            if not (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == '1'):
                return
            
            grid[row][col] = '0'
            
            for cr, cc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                dfs(row + cr, col + cc)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count