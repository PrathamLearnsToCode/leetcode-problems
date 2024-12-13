class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return False
            if grid[i][j] == 1 or (i,j) in visited:
                return True
            
            visited.add((i,j))
            
            top = dfs(i - 1, j)
            bottom = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            
            return top and bottom and left and right
        
        closed_inslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i,j) not in visited:
                    if dfs(i,j):
                        closed_inslands += 1
                        
        return closed_inslands