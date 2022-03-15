class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                ret.append(interval)
            
            elif newInterval[1] < interval[0]:
                ret.append(newInterval)
                newInterval = interval
                
            elif newInterval[1] > interval[0] or interval[1] > newInterval[0]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            
        ret.append(newInterval)
        
        return ret
                
        