class Solution:
    def minOperations(self, s: str) -> int:
        true_start, true_count = True, 0
        
        for i, ch in enumerate(s):
            
            if true_start != int(ch):
                true_count += 1
            
            true_start = not true_start

        return min(true_count, len(s) - true_count)