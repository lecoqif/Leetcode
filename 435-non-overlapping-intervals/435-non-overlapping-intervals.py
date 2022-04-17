class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        
        print(intervals)
        curr = intervals[0]
        
        toRemove = 0
        
        for i in range(1, len(intervals)):
            if curr[1] > intervals[i][0]:
                toRemove += 1
            
            else:
                curr = intervals[i]
        
        return toRemove