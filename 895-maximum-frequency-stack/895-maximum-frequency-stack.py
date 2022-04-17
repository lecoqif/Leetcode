class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.stacks = defaultdict(list)
        self.freqDict = defaultdict(int)
        

    def push(self, x: int) -> None:
        self.freqDict[x] += 1
        self.stacks[self.freqDict[x]].append(x)
        self.maxFreq = max(self.maxFreq, self.freqDict[x])

    def pop(self) -> int:
        val = self.stacks[self.maxFreq].pop()
        self.freqDict[val] -= 1
        
        if len(self.stacks[self.maxFreq]) == 0:
            self.maxFreq -= 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()