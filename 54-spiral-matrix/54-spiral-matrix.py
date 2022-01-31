class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rlow, rhigh = -1, len(matrix)
        clow, chigh = -1, len(matrix[0])
        
        rows, cols = len(matrix), len(matrix[0])
        
        crow, ccol = 0, 0
        
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        idx = 0
        
        ret = []
        
        while len(ret) < rows * cols:
            ret.append(matrix[crow][ccol])
            nrow, ncol = crow + dirs[idx][0], ccol + dirs[idx][1]
            
            if ncol in {chigh, clow} or nrow in {rhigh, rlow}:
                if ncol == chigh:
                    rlow += 1

                elif nrow == rhigh:
                    chigh -= 1

                elif ncol == clow:
                    rhigh -= 1
                
                elif nrow == rlow:
                    clow += 1
                
                idx = (idx + 1) % 4
                nrow, ncol = crow + dirs[idx][0], ccol + dirs[idx][1]
            
            crow, ccol = nrow, ncol
            
        return ret

                
            
            