class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ["+", "-", "*", "/"]
        for char in tokens:
            if char in operation:
                a = int(stack.pop())
                b = int(stack.pop())

                if char == "+":
                    stack.append(a+b)
                elif char == "-":
                    stack.append(b-a)
                elif char == "*":
                    stack.append(a*b)
                elif char == "/":
                    stack.append(int(b/a))
            
            else:
                stack.append(int(char))
            
            
        
        return stack[0]
