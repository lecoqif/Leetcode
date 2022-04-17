class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        stringSet = set()
        
        nums.sort()
        
        output = [[]]
        
        def createString(vals: List[int]) -> str:
            return ",".join(list(map(str, vals)))
        
        for i in nums:
            size = len(output)
            for j in range(size):
                temp = output[j][:]
                temp.append(i)
                stringTemp = createString(temp)
                
                if stringTemp not in stringSet:
                    output.append(temp)
                    stringSet.add(stringTemp)
        
        return output
                