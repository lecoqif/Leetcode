class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        
        n = len(intervals)
        
        if n == 0:
            return []
        
        intervals.sort(key=lambda x:x[0])
        
        curr = intervals[0]
        
        for i in range(1, n):
            if curr[1] < intervals[i][0]:
                ret.append(curr)
                curr = intervals[i]
            
            else:
                curr[1] = max(curr[1], intervals[i][1])
            
        ret.append(curr)
        
        return ret