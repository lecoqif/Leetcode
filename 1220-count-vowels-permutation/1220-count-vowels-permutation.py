class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        if n == 1: return 5
        
        hm = {x : 1 for x in ['a', 'e', 'i', 'o', 'u']}
        
        ret = 5
        
        for i in range(2, n + 1):
            new_hm = defaultdict(int)
            new_hm['e'] += hm['a'] + hm['i']
            new_hm['a'] += hm['e'] + hm['i'] + hm['u']
            new_hm['i'] += hm['e'] + hm['o']
            new_hm['u'] += hm['i'] + hm['o']
            new_hm['o'] += hm['i']
            
            ret += hm['e'] + 3 * hm['i'] + hm['o']
            
            hm = new_hm
        
        return ret % (10 ** 9 + 7)
            