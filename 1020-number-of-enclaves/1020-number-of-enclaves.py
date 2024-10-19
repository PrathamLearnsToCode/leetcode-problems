class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visit = set()
        def dfs(i,j):
            if i not in range(m) or j not in range(n) or grid[i][j] == 0:
                return
            
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        for i in range(m):
            for j in [0, n - 1]:
                if grid[i][j] == 1 and (i, j) not in visit:
                    dfs(i, j)
        
        for j in range(n):
            for i in [0, m - 1]:  
                if grid[i][j] == 1 and (i, j) not in visit:
                    dfs(i, j)
    
        enclave_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visit:
                    enclave_count += 1
        
        return enclave_count
                    
        
            
            
            
            
            
            
        