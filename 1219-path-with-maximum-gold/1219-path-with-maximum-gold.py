class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(i,j,current_gold):
            if i<0 or i>= len(grid) or j<0 or j>=len(grid[0]):
                return current_gold
            if grid[i][j] == 0 :
                return current_gold
            
            original_value = grid[i][j]
            current_gold += original_value
            grid[i][j] = 0
            maxi = max(
                dfs(i + 1, j, current_gold),
                dfs(i - 1, j, current_gold),
                dfs(i, j + 1, current_gold),
                dfs(i, j - 1, current_gold)
            )
            grid[i][j] = original_value
            return maxi
        
        max_gold_collected = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_gold_collected = max(max_gold_collected, dfs(i,j,0))
                    
        return max_gold_collected
            
            
        