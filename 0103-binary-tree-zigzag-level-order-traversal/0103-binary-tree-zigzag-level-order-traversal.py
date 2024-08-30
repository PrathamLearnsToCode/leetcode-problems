# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = collections.deque([root])
        zigZag = 1
        while q:
            qLen = len(q)
            sub_list = []

            for i in range(qLen):
                node = q.popleft()
                sub_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(sub_list[::zigZag])
            zigZag *= - 1
            
        return res
        