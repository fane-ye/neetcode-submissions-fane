class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+", "-", "*", "/"])
        
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            
            else: #is an operand
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(b/a) )
        
        return stack.pop()