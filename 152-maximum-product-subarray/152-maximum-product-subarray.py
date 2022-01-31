class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        posProduct = negProduct = nums[0]
        
        total = nums[0]
        
        for i in range(1, len(nums)):
            temp = max(posProduct * nums[i], max(negProduct * nums[i], nums[i]))
            negProduct = min(negProduct * nums[i], min(posProduct * nums[i], nums[i]))
            total = max(total, temp)
            posProduct = temp
            
        return total
            
        