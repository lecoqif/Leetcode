class Bucket:
    def __init__(self):
        self.chain = []
    
    def add(self, val: int) -> None:
        if not self.contains(val):
            self.chain.append(val)
    
    def remove(self, val: int) -> None:
        if not self.contains(val):
            return
        
        idx = self.chain.index(val)
        self.chain[-1], self.chain[idx] = self.chain[idx], self.chain[-1]
        self.chain.pop()
    
    def contains(self, val: int) -> bool:
        return val in self.chain

class MyHashSet:

    def __init__(self):
        self.length = 1000
        self.hashSet = [Bucket() for _ in range(self.length)]

    def computeHash(self, key):
        return key % self.length
        
    def add(self, key: int) -> None:
        self.hashSet[self.computeHash(key)].add(key)

    def remove(self, key: int) -> None:
        self.hashSet[self.computeHash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return self.hashSet[self.computeHash(key)].contains(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)