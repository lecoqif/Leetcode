class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        charFreq = [0] * 26
        
        for i in range(len(s)):
            charFreq[ord(s[i]) - ord('a')] += 1
            charFreq[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if charFreq[i] > 0:
                return False
        
        return True
        