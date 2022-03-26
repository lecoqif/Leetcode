from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charCount = [0 for _ in range(128)]
        
        for ch in t:
            charCount[ord(ch)] += 1
        
        left = right = 0
        
        n = len(s)
        
        ret = float('inf')
        retVal = ""
        
        while right < n:
            
            charCount[ord(s[right])] -= 1
            
            while self.check(charCount):
                if right - left + 1 < ret:
                    ret = right - left + 1
                    retVal = s[left:right + 1]
                charCount[ord(s[left])] += 1
                left += 1
                
            
            right += 1
            
        
        return retVal
    
    def check(self, countArr):
        for num in countArr:
            if num > 0:
                return False
        
        return True
            
            