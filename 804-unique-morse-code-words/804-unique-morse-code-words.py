class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        hm = {chr(i + 97): morse[i] for i in range(26)}
        
        seen = set()
        
        for word in words:
            translation = []
            for ch in word:
                translation.append(hm[ch])
            
            seen.add(''.join(translation))
        
        return len(seen)