class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        visit = set()
        start_color = image[sr][sc]
        if start_color == color:
            return image
        def dfs(i,j):
            if (i not in range(rows) or 
                j not in range(cols) or
                image[i][j] != start_color or
                (i, j) in visit):
                return
            visit.add((i,j))
            image[i][j] = color
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for dr, dc in directions:
                dfs(i+dr, j+dc)
                    
        dfs(sr,sc)
        return image
                    
                    
            
                
        
        