class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        if len(words) == 1:
            return "".join(set(words[0]))
        
        graph = defaultdict(list)
        
        in_degree = defaultdict(int)
        
        alphabet = set()
        
        for word1, word2 in zip(words, words[1:]):
            alphabet.update(word1)
            alphabet.update(word2)
            diff = False
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    graph[word1[i]].append(word2[i])
                    in_degree[word2[i]] += 1
                    diff = True
                    break
            
            if not diff and len(word1) > len(word2):
                return ""
                
        
        q = deque()
        
        for ch in alphabet:
            if in_degree[ch] == 0:
                q.append(ch)
        
        ret = []
        
        while q:
            curr = q.popleft()
            
            ret.append(curr)
            
            for nei in graph[curr]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return "".join(ret) if len(ret) == len(alphabet) else ""
            
                    
        