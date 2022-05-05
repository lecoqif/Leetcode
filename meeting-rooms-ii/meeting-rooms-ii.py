from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ret = 1
        
        intervals.sort(key=lambda x : x[0])
        
        rooms = [ (intervals[0][1], intervals[0]) ]
        
        for i in range(1, len(intervals)):
            end_time, interval = rooms[0]
            if intervals[i][0] >= end_time:
                heappop(rooms)
            
            heappush(rooms, (intervals[i][1], intervals[i]))
            ret = max(ret, len(rooms))
        
        return ret
            
            
        
        
        