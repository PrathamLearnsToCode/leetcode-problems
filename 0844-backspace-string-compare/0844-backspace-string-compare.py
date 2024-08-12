class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in s:
            if i!='#':
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
        
        for i in t:
            if i!='#':
                stack2.append(i)
            else:
                if stack2:
                    stack2.pop()
        
        if len(stack1)!=len(stack2):
            return False
        for i in range(len(stack1)):
            if stack1[i]!=stack2[i]:
                return False
        return True