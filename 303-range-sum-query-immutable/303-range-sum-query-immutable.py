class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        self.nums = nums
        self.populate_map()
    
    def populate_map(self):
        curr = 0
        
        for i in range(len(self.nums)):
            curr += self.nums[i]
            self.sums.append(curr)
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        
        return self.sums[right] - self.sums[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)