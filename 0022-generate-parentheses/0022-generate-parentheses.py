class Solution:
    def BackTrack(self, n, openp, closedp, stack, res):
        if openp == closedp == n:
            res.append("".join(stack))
            return
        
        if n>openp:
            stack.append('(')
            self.BackTrack(n, openp + 1, closedp, stack, res)
            stack.pop()
        
        if openp>closedp:
            stack.append(')')
            self.BackTrack(n, openp, closedp + 1, stack, res)
            stack.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        self.BackTrack(n,0,0,stack, res)
        return res
        
        