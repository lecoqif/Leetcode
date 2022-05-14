class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0 for _ in range(26)]
        
        left = right = 0
        
        n = len(s)
        
        ret = 0
        
        while right < n:
            count[ord(s[right]) - ord('A')] += 1
            maxf = max(count)
            
            while right - left + 1 > maxf + k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            ret = max(ret, right - left + 1)
            right += 1
        
        return ret
        
        