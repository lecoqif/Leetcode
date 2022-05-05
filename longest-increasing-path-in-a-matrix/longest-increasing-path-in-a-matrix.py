class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        seen = [[-1 for _ in range(COLS)] for i in range(ROWS)]
        
        def dfs(row: int, col: int):
            nonlocal ROWS, COLS
            
            if seen[row][col] != -1:
                return seen[row][col]
            
            neighbors = [[-1, 0], [0, -1], [0, 1], [1, 0]]
            
            currPath = 1
            longest = 0
            for nei in neighbors:
                newR, newC = row + nei[0], col + nei[1]
                if 0 <= newR < ROWS and 0 <= newC < COLS and matrix[newR][newC] > matrix[row][col]:
                    longest = max(longest, dfs(newR, newC))
            
            seen[row][col] = currPath + longest
            
            return seen[row][col]
        
        return max([dfs(i, j) for i in range(ROWS) for j in range(COLS)])