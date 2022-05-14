class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        
        def partition(arr: List[int], left: int, right: int):
            i = left
            
            pivot = arr[right]
            
            for j in range(left, right):
                if arr[j] <= arr[right]:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
            
            arr[right], arr[i] = arr[i], arr[right]
            return i

        
        while left <= right:
            pivot = partition(nums, left, right)
            
            if pivot == len(nums) - k:
                return nums[pivot]
            
            elif pivot < len(nums) - k:
                left = pivot + 1
            
            else:
                right = pivot - 1
        
        return -1