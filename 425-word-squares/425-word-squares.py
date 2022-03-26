class Node:
    def __init__(self, ch):
        self.ch = ch
        self.children = defaultdict(Node)
        self.isWord = False
        self.completeWord = ""

class Trie:
    def __init__(self):
        self.root = Node("/")
    
    def insert(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
            
            curr = curr.children[ch]
            
        curr.isWord = True
        curr.completeWord = word
    
    def startsWith(self, prefix) -> List[str]:
        curr = self.root
        
        for ch in prefix:
            if ch not in curr.children:
                return []
            
            curr = curr.children[ch]
        
        q = deque([curr])
        
        ret = []
        
        while len(q) > 0:
            node = q.popleft()
            
            if node.isWord:
                ret.append(node.completeWord)
            
            for ch in node.children:
                q.append(node.children[ch])
        
        return ret
         
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # b a l l
        # a r e a
        # l e a d
        # l a d y
        self.trie = Trie()
        
        self.n = len(words[0])
        
        self.words = words
        
        self.ret =[]
            
        list(self.trie.insert(word) for word in words)
        
        for word in words:
            output = [list('.' * self.n) for _ in range(self.n)]
            
            for i in range(len(word)):
                output[i][0] = word[i]
            
            output[0] = list(word)

            self.backtrack(output, 1)
        
        return self.ret
    
    def backtrack(self, output, idx):
        if idx == self.n:
            self.ret.append(list(map(lambda x:"".join(x), output)))
            return
        
        for word in self.trie.startsWith(output[idx][:idx]):
            temp = self.trie.startsWith(output[idx][:idx])
            output[idx] = list(word)
            
            for i in range(idx, len(word)):
                output[i][idx] = word[i]
            
            self.backtrack(output, idx + 1)
            
            output[idx][idx:] = list("." * (self.n - idx))
            
            for i in range(idx, len(word)):
                output[i][idx] = "."
            
            
        
        
        
        
        
        
        
        
        