class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        def backtrack(pos: int, curr: str, count: int) -> None:
            if pos == len(word):
                ret.append(curr + (str(count) if count > 0 else ''))
            
            else:
                backtrack(pos + 1, curr, count + 1)
                backtrack(pos + 1, curr + (str(count) if count > 0 else '') + word[pos], 0)
        
        ret = []
        
        backtrack(0, '', 0)
        
        return ret
                
                
                