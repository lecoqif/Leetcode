class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_len = len(words[0])
        
        counter = Counter(words)
        
        if len(s) < word_len * len(words): return []
        
        iter_start = word_len * len(words)
        
        ret = []
        
        for i in range(0, len(s) - iter_start + 1):
            curr_window = s[i: i + iter_start]
            
            curr_counter = Counter()
            
            for j in range(i, i + iter_start, word_len):
                curr_word = s[j: j + word_len]
                
                curr_counter[curr_word] += 1
            
            if curr_counter == counter: ret.append(i)
        
        
        return ret
                
            
            
                
            
            
            
                
            
                
            
        
        