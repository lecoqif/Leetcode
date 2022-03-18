class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        s1_char_count = [0 for _ in range(26)]
        
        n = len(s2)
        
        s2_char_count = s1_char_count[:]
        
        for ch in s1:
            s1_char_count[self.get_ord(ch)] += 1
        
        for i in range(len(s1)):
            s2_char_count[self.get_ord(s2[i])] += 1
        
        if s1_char_count == s2_char_count:
                return True
        
        while i < n - 1:
            i += 1
            
            s2_char_count[self.get_ord(s2[i])] += 1
            s2_char_count[self.get_ord(s2[i - len(s1)])] -= 1
            
            if s1_char_count == s2_char_count:
                return True
            
            
        return False
            
    def get_ord(self, ch):
        return ord(ch) - ord('a')