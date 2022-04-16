class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        
        odd = 0
        
        for key in counter:
            if counter[key] % 2 == 1:
                odd += 1
            
            if odd > 1:
                return False
        
        return True