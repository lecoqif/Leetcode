class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexMap = { val: idx for idx, val in enumerate(nums2) }
        
        nextArr = [-1] * len(nums2)
        
        stack = []
        
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            nextArr[i] = stack[-1] if stack else -1
            stack.append(nums2[i])
            

        return [nextArr[indexMap[i]] for i in nums1]
        
        