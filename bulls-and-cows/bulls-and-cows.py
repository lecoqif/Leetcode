class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        digitCount = [0] * 10
        
        for num in secret:
            digitCount[int(num)] += 1
        
        for x, y in zip(secret, guess):
            if x == y:
                bulls += 1
                digitCount[int(x)] -= 1
        
        for x, y in zip(secret, guess):
            if x != y and  digitCount[int(y)] > 0:
                cows += 1
                digitCount[int(y)] -= 1
                
        return f"{bulls}A{cows}B"
