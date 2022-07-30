class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        superSet = defaultdict(int)
        
        for word in words2:
            counter = Counter(word)
            
            for item, freq in counter.items():
                superSet[item] = max(superSet[item], freq)
        
        ret = []
        
        for word in words1:
            counter = Counter(word)
            
            flag = True
            for item in superSet:
                if superSet[item] > counter[item]:
                    flag = False
                    break
            
            if flag:
                ret.append(word)
        
        return ret
                
                
                
                