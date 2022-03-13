from collections import Counter, defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        
        ldict = Counter(s)
        
        fdict = defaultdict(list)
        
        for l in ldict.keys():
            fdict[ldict[l]].append(l)
            
        max_key = max(fdict.keys())
        
        ret = 0
        
        while max_key > 0:
            while len(fdict[max_key]) > 1:
                curr = fdict[max_key].pop()
                fdict[max_key - 1].append(curr)
                ret += 1
                
            max_key -= 1
        
        return ret
                
                       
                       
            
            
            
         
        