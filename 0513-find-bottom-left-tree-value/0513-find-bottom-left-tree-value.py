# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        q = collections.deque([root])
        bottom_left = root.val
        while q:           
            qLen = len(q)
            for i in range(qLen):                
                node = q.popleft()
                if i == 0:
                    bottom_left = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return bottom_left
                    
            
                
        