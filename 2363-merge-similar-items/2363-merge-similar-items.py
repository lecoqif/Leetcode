class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hm = defaultdict(int)
        
        for value, weight in items1 + items2:
            hm[value] += weight
        
        return sorted([[value, hm[value]] for value in hm])