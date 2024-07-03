# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      
      self.diameter = 0
      
      def helper(root):
        if not root:
          return 0

        lh = helper(root.left)
        rh = helper(root.right)
        self.diameter = max(lh+rh, self.diameter)
        
        height = 1 + max(lh,rh)

        return height
      
      helper(root)
      return self.diameter