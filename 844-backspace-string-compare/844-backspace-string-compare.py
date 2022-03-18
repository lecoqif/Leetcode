class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        Sq, Tq = deque(), deque()
        
        for ch in S:
            if ch != '#':
                Sq.append(ch)
            else:
                if len(Sq) > 0:
                    Sq.pop()
        
        for ch in T:
            if ch != '#':
                Tq.append(ch)
            else:
                if len(Tq) > 0:
                    Tq.pop()
        
        return Sq == Tq
        
        
            
            
        