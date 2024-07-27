class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stack = []
      for i in tokens:
        if i not in ('+','-','*','/'):
          stack.append(int(i))
        elif i == '+':
          stack.append(stack.pop() + stack.pop())
        elif i == '*':
          stack.append(stack.pop() * stack.pop())
        elif i == '/':
          a = stack.pop()
          b = stack.pop()
          stack.append(int(b/a))
        elif i == '-':
          a = stack.pop()
          b = stack.pop()
          stack.append(b-a)
      
      return stack[0]
        
        