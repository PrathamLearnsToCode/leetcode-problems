class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        row = [0] * n
        col = [0] * m
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
                    
                    
        for i in range(n):
            for j in range(m):
                if row[i]==1 or col[j]==1:
                    matrix[i][j] = 0
                    
                    
        return matrix
                    
        