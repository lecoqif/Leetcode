class Solution:
    def decodeString(self, s: str) -> str:
        numStack, letterStack = [], []

        currStr, currNum = "", 0
        
        for i in s:
            if i.isdigit():
                currNum = currNum * 10 + int(i)
            elif i.isalpha():
                currStr += i
            elif i == '[':
                numStack.append(currNum)
                letterStack.append(currStr)
                currStr = ""
                currNum = 0
            elif i == ']':
                prevStr = letterStack.pop()
                prevNum = numStack.pop()
                currStr = prevStr + prevNum * currStr
        
        return currStr
                
        