from collections import defaultdict

class Node:
    def __init__(self, ch):
        self.ch = ch
        self.children = defaultdict(Node)
        self.isComplete = False
        self.completeText = ""

class Trie:
    def __init__(self):
        self.root = Node("/")
        self.currNode = self.root
    
    def insert(self, text):
        curr = self.root
        
        for ch in text:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
            
            curr = curr.children[ch]
        
        curr.isComplete = True
        curr.completeText = text
    
    def reset(self):
        self.currNode = self.root
    
    def startsWith(self, prefix) -> List[str]:
        
        for ch in prefix:
            if ch not in self.currNode.children:
                self.currNode = Node("")
                return []
            
            self.currNode = self.currNode.children[ch]
        
        curr = self.currNode
        
        q = deque([curr])
        
        ret = []
        
        while len(q) > 0:
            node = q.popleft()
            
            if node.isComplete:
                ret.append(node.completeText)
            
            for ch in node.children:
                q.append(node.children[ch])
        
        return ret

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.hotDict = { sentence: time for sentence, time in zip(sentences, times) }
        self.trie = Trie()
        self.buildTrie(sentences)
        self.inputSentence = ""
    
    def buildTrie(self, sentences: List[str]) -> None:
        for sentence in sentences:
            self.trie.insert(sentence)

    def input(self, c: str) -> List[str]:
        if c == '#' and self.inputSentence != "":
            self.trie.insert(self.inputSentence)
            self.hotDict[self.inputSentence] = self.hotDict.get(self.inputSentence, 0) + 1
            self.inputSentence = ""
            self.trie.reset()
            return []
        else:
            self.inputSentence += c
            allSentences = self.trie.startsWith(c)
            allSentences.sort(key=lambda x: (-self.hotDict[x], x))
            return allSentences[:3]

        
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)