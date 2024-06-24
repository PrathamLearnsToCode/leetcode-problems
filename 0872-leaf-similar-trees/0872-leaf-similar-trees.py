# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafList1 = []
        leafList2 = []
        def dfs(root, leafList):
            if not root:
                return
            
            if not root.left and not root.right:
                leafList.append(root.val)
                
            dfs(root.left, leafList)
            dfs(root.right, leafList)
            
            return leafList
        
        dfs(root1, leafList1)
        dfs(root2, leafList2)
        
        return leafList1==leafList2
                
        