class MyStack:

    def __init__(self):
        self.push_q = []
        self.pop_q = []
        self.peek = None
        

    def push(self, x: int) -> None:
        self.push_q.append(x)
        self.peek = x
        

    def pop(self) -> int:
        while len(self.push_q) > 1:
            val = self.push_q.pop(0)
            self.pop_q.append(val)
            self.peek = val
        
        ret = self.push_q.pop(0)
        self.push_q, self.pop_q = self.pop_q, self.push_q
        return ret
        
    def top(self) -> int:
        return self.peek
        
        
    def empty(self) -> bool:
        return len(self.push_q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()