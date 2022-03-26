class Node:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.word = False
        
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
    
    def findPairs(self, text) -> List[List[int]]:
        ret = []
        
        for i in range(len(text)):
            idx = start = i
            curr = self.root
            while idx < len(text) and text[idx] in curr.children:
                curr = curr.children[text[idx]]
                if curr.word:
                    ret.append([start, idx])
                idx += 1
        
        return ret

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        return trie.findPairs(text)
        