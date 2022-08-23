class Solution:
    def minOperations(self, s: str) -> int:
        true_start, false_start, true_count, false_count = True, False, 0, 0
        
        for i, ch in enumerate(s):
            val = int(ch)
            
            if true_start != val:
                true_count += 1
            
            if false_start != val:
                false_count += 1
            
            true_start = not true_start
            false_start = not false_start
        
        return min(true_count, false_count)