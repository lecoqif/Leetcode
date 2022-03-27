class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated = {
            "1": "1",
            '6': '9',
            '9': '6',
            '8': '8',
            '0': '0'
        }
        
        if not all(ch in rotated for ch in num): return False
        
        rotated_num = "".join(list(map(lambda x: rotated[x] if x in rotated else x, list(num)))[::-1])
        
        return num == rotated_num