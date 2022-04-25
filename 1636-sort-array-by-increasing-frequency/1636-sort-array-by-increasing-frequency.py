class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        
        res = []
        
        sortedKeys = sorted(counter.keys(), key=lambda x : (counter[x], -x))
        
        for key in sortedKeys:
            times = counter[key]
            for i in range(times):
                res.append(key)
        
        return res