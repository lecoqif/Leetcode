class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(left, right, curr):
            if left == n and right == n:
                ret.append("".join(curr))
                return
            
            if left < n:
                curr.append('(')
                generate(left + 1, right, curr)
                curr.pop()
            
            if right < left:
                curr.append(')')
                generate(left, right + 1, curr)
                curr.pop()
                
        
        ret = []
        generate(0, 0, [])
        return ret
            
        