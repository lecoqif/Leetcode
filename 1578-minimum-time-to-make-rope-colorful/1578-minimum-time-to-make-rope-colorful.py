class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ret = 0
        
        prev = 0
        
        for i in range(1, len(colors)):
            if colors[i] == colors[prev]:
                ret += min(neededTime[i], neededTime[prev])
                if neededTime[i] >= neededTime[prev]:
                    prev = i
            
            else:
                prev = i
        
        return ret
                
        
        