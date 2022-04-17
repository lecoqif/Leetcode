class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []
        
        @lru_cache
        def isPalindrome(word: str) -> bool:
            if len(word) == 0: return False
            
            for i in range(len(word) // 2):
                if word[i] != word[len(word) - 1 - i]:
                    return False
            
            return True
        
        def dfs(word: str, curr: List[str]) -> None:
            if len(word) == 0:
                output.append(curr[:])
                return
            
            for i in range(len(word)):
                currWord = word[0:i + 1]
                if isPalindrome(currWord):
                    curr.append(currWord)
                    dfs(word[i + 1:], curr)
                    curr.pop()
        
        dfs(s, [])
        return output
                    