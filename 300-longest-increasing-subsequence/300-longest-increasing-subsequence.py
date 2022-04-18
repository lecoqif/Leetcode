class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        
        def findInsertPos(arr: List[int], val: int) -> int:
            start, end = 0, len(arr) - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if arr[mid] >= val:
                    end = mid - 1
                
                else:
                    start = mid + 1
            
            return start
             
        for i, num in enumerate(nums):
            insertPos = findInsertPos(lis, num)
            if insertPos == len(lis):
                lis.append(num)
            
            else:
                lis[insertPos] = num
        
        return len(lis)
            
            
    