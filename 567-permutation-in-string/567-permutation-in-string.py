class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        s1_char_count = [0 for _ in range(26)]
        
        s2_char_count = s1_char_count[:]
        
        for i in range(len(s1)):
            s1_char_count[self.get_ord(s1[i])] += 1
            s2_char_count[self.get_ord(s2[i])] += 1
        
        for i in range(len(s2) - len(s1)):
            
            if s1_char_count == s2_char_count:
                    return True
            
            s2_char_count[self.get_ord(s2[i + len(s1)])] += 1
            s2_char_count[self.get_ord(s2[i])] -= 1
            
        return s1_char_count == s2_char_count
            
    def get_ord(self, ch):
        return ord(ch) - ord('a')