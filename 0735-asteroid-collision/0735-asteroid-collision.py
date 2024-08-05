class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
      stack = []
      
      for i in asteroids:
        
        while stack and i<0<stack[-1]:
          if stack[-1] < -i:
            stack.pop()
            continue
          elif stack[-1] == -i:
            stack.pop()            
          break
        else:
          stack.append(i)
          
      return stack
          
        