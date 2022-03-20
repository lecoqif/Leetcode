class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        phone = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7:"pqrs", 8: "tuv", 9: "wxyz"}
        
        ret = []
        
        def backtrack(idx=0, curr=[]):
            if idx == len(digits):
                ret.append("".join(curr[:]))
                return
            
            for digit in phone[int(digits[idx])]:
                curr.append(digit)
                backtrack(idx+1, curr)
                curr.pop()
            
        backtrack()
        
        return ret