class Node:
    def __init__(self, ch) -> None:
        self.ch = ch
        self.children = {}
        self.word = False

class Trie:
    def __init__(self) -> None:
        self.root = Node("/")
    
    def insert(self, word) -> None:
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
            
            curr = curr.children[ch]
        
        curr.word = True
    
    def checkLongest(self, word) -> bool:
        curr = self.root
        
        for ch in word:
            curr = curr.children[ch]
            if not curr.word:
                return False
        
        return True   

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        maxLen = 0
        
        ret = ""
        
        for word in words:
            
            if trie.checkLongest(word) and len(word) >= maxLen:
                if len(word) == maxLen and word < ret or len(word) > maxLen:
                    ret = word
                    maxLen = len(word)
        
        return ret
                
        
        
        
        
        