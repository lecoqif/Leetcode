class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = Counter(s)
        
        return "".join(sorted(list(s), key=lambda x : (-char_counts[x], x)))
        