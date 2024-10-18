class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        
        rows = len(mat)
        cols = len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r,c))
                else:
                    dist[r][c] = float('inf')
                    
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            r,c = queue.popleft()
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if 0<= nr <rows and 0 <= nc < cols:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr,nc))
                        
        return dist