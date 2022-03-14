class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        
        for num in nums:
            place = self.binSearch(lis, num) 
            
            if place == len(lis):
                lis.append(num)
            
            else:
                lis[place] = num
            
        return len(lis)
    
    def binSearch(self, nums, val):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] < val:
                start = mid + 1
                
            else:
                end = mid - 1
        
        return start
                
        