class Solution {
    func mergeSimilarItems(_ items1: [[Int]], _ items2: [[Int]]) -> [[Int]] {
        var someDict = [Int: Int]()
        
        for kv in items1 + items2 {
            someDict[kv[0], default: 0] += kv[1]
        }
        
        var someInts:[[Int]] = []
        
        for (key, value) in someDict {
            someInts.append([key, value])
        }
        
        return someInts.sorted(by: { $0[0] < $1[0] })
    }
}