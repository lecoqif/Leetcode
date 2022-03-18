class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"):
                return
            
            grid[row][col] = "0"
            
            ranges = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            
            for way in ranges:
                dfs(row + way[0], col + way[1])
        
        
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ret += 1
                    dfs(i, j)
        
        return ret
                