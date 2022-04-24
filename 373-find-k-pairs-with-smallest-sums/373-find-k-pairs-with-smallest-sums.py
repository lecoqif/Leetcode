from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        i = j = count = 0
        
        heappush(heap, (nums1[i] + nums2[j], i, j))
        
        ret = []
        
        while heap:
            curr, i, j = heappop(heap)
            ret.append((nums1[i], nums2[j]))
            count += 1
            
            if count == k:
                break
            
            if i + 1 < len(nums1):
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            
            if i == 0 and j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            #   1   7   11
            # 2 x   x
            # 4 x
            # 6

        return ret