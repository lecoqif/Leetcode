class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        is_flush = all(suits[i] == suits[0] for i in range(5))
        
        if is_flush: return "Flush"
        
        counter = Counter(ranks)
        
        for rank, freq in counter.most_common():
            if freq >= 3:
                return "Three of a Kind"
            
            elif freq == 2:
                return "Pair"
        
        return "High Card"
        
        