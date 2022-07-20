class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hm = [[] for _ in range(26)]
        
        
        for word in words:
            idx = ord(word[0]) - ord('a')
            hm[idx].append(word)
        
        ret = 0
        
        for ch in s:
            idx = ord(ch) - ord('a')
            matches = hm[idx]
            
            size = len(matches)
            
            for i in range(size):
                word = matches.pop(0)
                if len(word) == 1:
                    ret += 1
                
                else:
                    new_idx = ord(word[1:][0]) - ord('a')
                    hm[new_idx].append(word[1:])
            
        return ret
            