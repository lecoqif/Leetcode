class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right, n = 0, 0, len(fruits)
        
        ret = 0
        
        hm = {}
        
        while right < n:
            hm[fruits[right]] = hm.get(fruits[right], 0) + 1
            
            while len(hm.keys()) > 2:
                hm[fruits[left]] -= 1
                if hm[fruits[left]] == 0:
                    del hm[fruits[left]]
                left += 1
            
            ret = max(ret, right - left + 1)
            
            right += 1
        
        return ret
            