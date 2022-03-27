class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        text = "".join(s.split("-")).upper()[::-1]
        
        ret = []
        
        for i in range(0, len(text), k):
            ret.append(text[i:i + k][::-1])
        
        return "-".join(ret[::-1])
        
