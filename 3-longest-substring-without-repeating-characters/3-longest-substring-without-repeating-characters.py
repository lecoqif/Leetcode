class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        
        left, right, ret = 0, 0, 0
        
        n = len(s)
        
        while right < n:
            if s[right] in hm:
                left = max(left, hm[s[right]] + 1)
                
            hm[s[right]] = right
            
            ret = max(ret, right - left + 1)
            
            right += 1
            
        return ret
        
        