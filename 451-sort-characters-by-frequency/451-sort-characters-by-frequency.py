class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = Counter(s)
        
        max_freq = 0
        
        for key in char_counts:
            max_freq = max(max_freq, char_counts[key])
        
        buckets = [[] for _ in range(max_freq + 1)]
        
        for key in char_counts:
            buckets[char_counts[key]].append(key)
        
        ret = ""
        
        for i in range(len(buckets) - 1, -1, -1):
            for val in buckets[i]:
                ret += val * i
        
        return ret
            