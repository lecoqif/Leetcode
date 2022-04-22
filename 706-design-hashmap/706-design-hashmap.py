class Bucket:
    def __init__(self):
        self.nodes = []
    
    def insert(self, key: int, val: int):
        for i, kv in enumerate(self.nodes):
            if kv[0] == key:
                self.nodes[i] = (key, val)
                return
        
        self.nodes.append((key, val))
    
    def get(self, key: int) -> int:
        for k, v in self.nodes:
            if k == key:
                return v
        
        return -1
    
    def remove(self, key: int) -> None:
        for i, kv in enumerate(self.nodes):
            if kv[0] == key:
                self.nodes[i] = self.nodes[-1]
                self.nodes.pop()
                return
        
        

class MyHashMap:

    def __init__(self):
        self.key_space = 769
        self.hash_map = [Bucket() for _ in range(self.key_space)]

    def hash_val(self, key: int) -> int:
        return key % self.key_space
        
    def put(self, key: int, value: int) -> None:
        self.hash_map[self.hash_val(key)].insert(key, value)

    def get(self, key: int) -> int:
        return self.hash_map[self.hash_val(key)].get(key)

    def remove(self, key: int) -> None:
        self.hash_map[self.hash_val(key)].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)