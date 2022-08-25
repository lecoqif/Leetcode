class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        
        elements = list(sorted(counter.keys()))
        
        ret = 0
        
        for el in elements[1:-1]:
            ret += counter[el]
        
        return ret
                