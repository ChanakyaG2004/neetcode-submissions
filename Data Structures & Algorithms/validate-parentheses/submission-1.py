class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for b in s:
            if b == '{' or b == '[' or b == '(':
                stack.append(b) 
            elif b == '}':
                if not stack:
                    return False
                if stack.pop() == '{':
                    continue
                else:
                    return False

            elif b == ']':
                if not stack:
                    return False
                if stack.pop() == '[':
                    continue
                else:
                    return False
            
            elif b == ')':
                if not stack:
                    return False
                if stack.pop() == '(':
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
            
            
