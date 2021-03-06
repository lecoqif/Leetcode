class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        
        stack = []
        
        for token in tokens:
            if token in operations:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(operations[token](num1, num2))

            else:
                stack.append(int(token))
        
        return stack.pop()
                
                
        