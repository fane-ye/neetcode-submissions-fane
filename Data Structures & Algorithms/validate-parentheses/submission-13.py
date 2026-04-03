class Solution:
    def isValid(self, s: str) -> bool:
        open_br = '([{'
        stack = []
        n = len(s)
        # read string on to stack
        # once its no longer an open char
        #start popping off stack and check for corresponding closed bracket
        for ch in s:
            if ch in open_br:
                stack.append(ch)

            else:
                if ch is None:
                    return False
                if not stack:
                    return False
                if ch == ']' and  stack[-1]=='[':
                    stack.pop()
                    continue
                if ch == '}' and  stack[-1]=='{':
                    stack.pop()                    
                    continue
                if ch == ')' and  stack[-1]=='(':
                    stack.pop()                    
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
            
        return False

            
            
            
        
        
                
            


            


        
        # if open and then other is open must clsoe in same order of open