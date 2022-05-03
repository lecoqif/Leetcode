from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, (-num, num))
        
        if self.maxHeap and self.minHeap and self.maxHeap[0][1] > self.minHeap[0][1]:
            _, val = heappop(self.maxHeap)
            heappush(self.minHeap, (val, val))
        
        if len(self.maxHeap) > (len(self.minHeap) + 1):
            _, val = heappop(self.maxHeap)
            heappush(self.minHeap, (val, val))
        
        if len(self.minHeap) > (len(self.maxHeap) + 1):
            _, val = heappop(self.minHeap)
            heappush(self.maxHeap, (-val, val))
        
        self.size += 1


    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (self.maxHeap[0][1] + self.minHeap[0][1]) / 2
        
        return self.maxHeap[0][1] if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0][1]
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()