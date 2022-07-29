class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def check_converted(word: str) -> bool:
            
            mapping = {}
            seen = set()
            
            ret = ''
            
            for ch, actual in zip(word, pattern):
                if ch not in mapping and actual not in seen:
                    mapping[ch] = actual
                    seen.add(actual)
                    ret += actual
                
                elif ch in mapping:
                    ret += mapping[ch]
                    
                else:
                    return False
            
            return ret == pattern
        
        ret = []
        
        for word in words:
            if check_converted(word):
                ret.append(word)
        
        return ret
            
        
        
        
        
        
        
                