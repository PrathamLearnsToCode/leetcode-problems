# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_table = defaultdict(list)
        
        def dfs(root, row, col):
            if not root:
                return
            
            col_table[col].append((row, root.val))
            
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
            
        dfs(root,0,0)
        
        result = []
        for col in sorted(col_table.keys()):
            result.append([val for row,val in sorted(col_table[col], key = lambda x: (x[0],x[1]))])
            
        return result