class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        def dfs(i,j):
            if (i not in range(rows) or
               j not in range(cols) or
               board[i][j] != "O"):
                return
            board[i][j] = "T"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i in [0, rows - 1] or j in [0, cols - 1]):
                    dfs(i,j)
                    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
                    
        
            
        