class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ret = ""
        
        sources = {x:y for x, y in zip(indices, sources)}
        targets = {x:y for x, y in zip(indices, targets)}
        
        indices.sort()
        
        prev = 0
        
        for idx in indices:
            ret += s[prev:idx]
            if s[idx: idx + len(sources[idx])] == sources[idx]:
                ret += targets[idx]
                prev = idx + len(sources[idx])
            else:
                prev = idx
        
        ret += s[prev:]
        
        return ret
        