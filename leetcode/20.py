class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif not stack:
                return False
            elif char == ')':
                if stack.pop() != '(':
                    return False
            elif char == ']':
                if stack.pop() != '[':
                    return False
            elif char == '}':
                if stack.pop() != '{':
                    return False
                
        return not stack