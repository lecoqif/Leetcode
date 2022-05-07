from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not endWord or not beginWord:
            return 0
        
        graph = defaultdict(list)
        
        for i, word in enumerate(wordList):
            for i in range(len(word)):
                newWord = word[0:i] + '.' + word[i + 1:]
                graph[newWord].append(word)
        
        seen = set()
        
        q = deque()
        
        q.append((beginWord, 1))
        
        while q:
            currWord, length = q.popleft()
            
            if currWord == endWord:
                return length
            
            seen.add(currWord)
            
            for i in range(len(currWord)):
                newWord = currWord[0:i] + '.' + currWord[i + 1:]
                
                for nei in graph[newWord]:
                    if nei not in seen:
                        q.append((nei, length + 1))
        
        return 0