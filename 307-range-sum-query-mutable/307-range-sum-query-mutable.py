class NumArray:

    def __init__(self, nums: List[int]):
        self.l = len(nums)
        self.seg_tree = [0] * self.l + nums
        self.nums = nums
        
        for i in range(self.l - 1, 0, -1):
            self.seg_tree[i] = self.seg_tree[i << 1] + self.seg_tree[(i << 1) | 1]

    def update(self, index: int, val: int) -> None:
        tree_index = index + self.l
        self.seg_tree[tree_index] = val
        while tree_index > 1:
            self.seg_tree[tree_index >> 1] = self.seg_tree[tree_index] + self.seg_tree[tree_index ^ 1]
            tree_index >>= 1
        
    def sumRange(self, left: int, right: int) -> int:
        left += self.l
        right += self.l
        
        ans = 0
        
        while left <= right:
            if left & 1:
                ans += self.seg_tree[left]
                left += 1
            
            left >>= 1
            
            if right & 1 == 0:
                ans += self.seg_tree[right]
                right -= 1
            
            right >>= 1
        
        return ans
                
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)