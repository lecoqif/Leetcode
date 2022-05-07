from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        graph = defaultdict(list)
        
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        for i, word in enumerate(wordList):   
            for i in range(len(word)):
                newWord = word[0:i] + '.' + word[i + 1:]
                graph[newWord].append(word)
        
        q = deque()
        
        seen = set()
        
        q.append((beginWord, 1))
        
        while q:
            currWord, length = q.popleft()
            
            if currWord == endWord:
                return length
            
            seen.add(currWord)
            
            for i in range(len(currWord)):
                graphIndex = currWord[0:i] + '.' + currWord[i + 1:]
                for nei in graph[graphIndex]:
                    if nei not in seen:
                        q.append((nei, length + 1))
        
        return 0
                
        
        
            
        
        