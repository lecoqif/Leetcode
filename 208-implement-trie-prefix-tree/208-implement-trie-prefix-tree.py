class Node:
    def __init__(self, ch):
        self.ch = ch
        self.children = {} 
        self.word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("/")
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
            
            curr = curr.children[ch]
        
        curr.word = True
        
    def traverseTrie(self, word: str) -> Node:
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                return None
            
            curr = curr.children[ch]
        
        return curr
        
        
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.traverseTrie(word)
        
        return node and node.word
        
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        node = self.traverseTrie(prefix)
        
        return node is not None
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)