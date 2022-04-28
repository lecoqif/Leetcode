class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        def expandAroundCentre(left: int, right: int) -> int:
            ret = 0
            nonlocal n
            
            while left >= 0 and right < n and s[left] == s[right]:
                ret += 1
                left -= 1
                right += 1
            
            return ret
            
            
        palindromes = 0
        
        for i in range(n):
            palindromes += expandAroundCentre(i, i)
            palindromes += expandAroundCentre(i, i + 1)
        
        return palindromes
            
    
    