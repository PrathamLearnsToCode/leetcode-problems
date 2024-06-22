class Solution:
    def isValid(self, s: str) -> bool:
        
        brack_map = {")":"(", "}":"{", "]":"["}
        
        stack = []
        
        for char in s:
            if char in brack_map:
                if stack and stack[-1] == brack_map[char]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(char)
                
        return True if not stack else False
                
                
        