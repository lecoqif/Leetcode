class MyStack:

    def __init__(self):
        self.push_q = []
        self.pop_q = []
        

    def push(self, x: int) -> None:
        self.push_q.append(x)
        
    def transfer(self):
        temp = []
        
        while self.push_q:
            temp.append(self.push_q.pop(0))
        
        for num in temp:
            self.pop_q.insert(0, num)

    def pop(self) -> int:
        self.transfer()
        return self.pop_q.pop(0)
        
    def top(self) -> int:
        self.transfer()
        return self.pop_q[0]
        
        
    def empty(self) -> bool:
        return len(self.push_q) == 0 and len(self.pop_q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()