class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = []
        
        def backtrack(word=s, idx=0, curr=deque()):
            if idx == len(word):
                ret.append("".join(curr))
                return
            
            if s[idx].isalpha():
                curr.append(s[idx].lower())
                
                backtrack(word, idx+1, curr)
                
                curr.pop()
                
                curr.append(s[idx].upper())

            else:
                curr.append(s[idx])
            
            backtrack(word, idx + 1, curr)
            
            curr.pop()
                
        
        backtrack()
        
        return ret