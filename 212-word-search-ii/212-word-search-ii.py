class Node:
    def __init__(self, ch):
        self.ch = ch
        # Letter --> Node
        self.children = {}
        self.isWord = False
        self.fullWord = ""
        self.parent = None
    
class Trie:
    def __init__(self):
        self.root = Node('/')
    
    def insertWord(self, word) -> None:
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
                curr.children[ch].parent = curr

            curr = curr.children[ch]
        
        curr.isWord = True
        curr.fullWord = word
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        
        for word in words:
            trie.insertWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        
        res = []
        
        def backtrack(row: int, col: int, node: Node) -> None:
            if not (0 <= row < ROWS and 0 <= col < COLS and board[row][col] in node.children):
                return 
            
            temp = board[row][col]
            
            newNode = node.children[board[row][col]]
            
            if newNode.isWord:
                res.append(newNode.fullWord)
                newNode.isWord = False
                
                curr = newNode
                
                while len(curr.children) == 0 and curr.ch != '/':
                    parent = curr.parent
                    parent.children.pop(curr.ch)
                    curr = parent
            
            board[row][col] = '#'
            
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            
            for neighbor in directions:
                backtrack(row + neighbor[0], col + neighbor[1], newNode)
            
            board[row][col] = temp
            
        for i in range(ROWS):
            for j in range(COLS):
                backtrack(i, j, trie.root)
        
        return res