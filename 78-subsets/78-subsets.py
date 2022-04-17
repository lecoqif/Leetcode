class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        
        for i in nums:
            size = len(output)
            for j in range(size):
                temp = output[j][:]
                temp.append(i)
                output.append(temp)
        
        return output