class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        total_sum = 0
        
        for i in range(m):
            for j in range(n):
                if i==j:
                    total_sum +=  mat[i][j]
                if (i + j) == len(mat) - 1:
                    total_sum += mat[i][j]
        if m==n and m%2==1 and n%2==1:
            total_sum = total_sum - mat[m//2][n//2]
                    
        return (total_sum)
                    
            
        