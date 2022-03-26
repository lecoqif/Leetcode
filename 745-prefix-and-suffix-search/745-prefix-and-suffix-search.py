class Node:
    def __init__(self, ch):
        self.ch = ch 
        self.children = {}
        self.word = False
        self.fullWord = ""

class Trie:
    def __init__(self):
        self.root = Node("/")
    
    def insert(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
            
            curr = curr.children[ch]
        
        curr.word = True
        curr.fullWord = word
    
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
            
            if node.word:
                ret.append(node.fullWord)
            
            for key in node.children:
                q.append(node.children[key])
        
        return ret
           
            
class WordFilter:

    def __init__(self, words: List[str]):
        self.wordDict = { word: i for i, word in enumerate(words) }
        self.words = words
        self.prefixTrie = Trie()
        self.suffixTrie = Trie()
        self.initTries()
    
    def initTries(self):
        for word in self.words:
            self.prefixTrie.insert(word)
            self.suffixTrie.insert(word[::-1])
        
    def f(self, prefix: str, suffix: str) -> int:
        prefixList = set(self.prefixTrie.startsWith(prefix))
        
        ret = -1
        
        for word in self.suffixTrie.startsWith(suffix[::-1]):
            word = word[::-1]
            if word in prefixList:
                ret = max(ret, self.wordDict[word])
        
        return ret
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)