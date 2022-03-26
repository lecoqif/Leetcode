from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCharCount = Counter(t)
        
        left = right = 0
        
        n = len(s)
        
        sCharCount = defaultdict(int)
        
        ret = float('inf')
        retVal = ""
        
        while right < n:
            
            sCharCount[s[right]] += 1
            
            while self.check(sCharCount, tCharCount):
                if right - left + 1 < ret:
                    ret = right - left + 1
                    retVal = s[left:right + 1]
                sCharCount[s[left]] -= 1
                left += 1
                
            
            right += 1
            
        
        return retVal
    
    def check(self, sDict, tDict):
        for key in tDict:
            if sDict[key] < tDict[key]:
                return False
        
        return True
            
            