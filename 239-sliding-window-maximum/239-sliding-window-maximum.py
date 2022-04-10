from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.q = deque()
        
    def push(self, val: int) -> None:
        while self.q and self.q[0] < val:
            self.q.popleft()
        self.q.appendleft(val)
    
    def pop(self, val: int) -> None:
        if self.q and self.q[-1] == val:
            self.q.pop()
        
    def max_val(self) -> None:
        return self.q[-1]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonicQueue = MonotonicQueue()
        res = []
        
        for i in range(len(nums)):
            if i < k - 1:
                monotonicQueue.push(nums[i])
            else:
                monotonicQueue.push(nums[i])
                res.append(monotonicQueue.max_val())
                monotonicQueue.pop(nums[i - k + 1])
        
        return res
                
        
        