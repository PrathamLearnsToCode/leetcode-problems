class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        self.dfs(root, res)
        return "".join(res)

    def dfs(self, t: TreeNode, res: list):
        if t is None:
            return
        res.append(str(t.val))

        if t.left is None and t.right is None:
            return
        res.append('(')

        self.dfs(t.left, res)
        res.append(')')

        if t.right is not None:
            res.append('(')

            self.dfs(t.right, res)
            res.append(')')
            