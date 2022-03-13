class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        
        ret = letters[0]
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            if letters[mid] > target:
                ret = letters[mid]
                end = mid - 1
            
            else:
                start = mid + 1
        
        return ret
                