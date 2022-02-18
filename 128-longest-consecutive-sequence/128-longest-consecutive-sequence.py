class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        
        longest_sequence = 0
        
        for num in nums:
            hm[num] = True
        
        for num in nums:
            if not hm[num]:
                continue
            
            curr_len = 1
            
            curr = num
            
            while curr - 1 in hm and hm[curr - 1]:
                hm[curr - 1] = False
                curr_len += 1
                curr = curr - 1
            
            curr = num
            
            while curr + 1 in hm and hm[curr + 1]:
                hm[curr + 1] = False
                curr_len += 1
                curr = curr + 1
            
            longest_sequence = max(longest_sequence, curr_len)
        
        return longest_sequence
            
            
            
            
        