from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        
        for num in nums:
            val = bisect_left(lis, num)
            if val == len(lis):
                lis.append(num)
            else:
                lis[val] = num
        
        return len(lis)
            