class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx1, idx2 = 0, 0
        
        ret = []
        
        while idx1 != len(firstList) and idx2 != len(secondList):
            int1, int2 = firstList[idx1], secondList[idx2]
            
            if int1[0] <= int2[0] and int1[1] >= int2[0] or int2[0] <= int1[0] and int2[1] >= int1[0]:
                start = max(int1[0], int2[0])
                end = min(int1[1], int2[1])
                ret.append([start, end])
            
            if int1[1] <= int2[1]:
                idx1 += 1
            else:
                idx2 += 1
            
        return ret