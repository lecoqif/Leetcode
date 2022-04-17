class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        
        @lru_cache(maxsize=None)
        def dfs(word: str) -> bool:
            if len(word) == 0:
                return True
            
            for i in range(len(word) + 1):
                if word[0:i] in wordSet and dfs(word[i:]):
                    return True
            
            return False
        
        return dfs(s)
                    
            
            