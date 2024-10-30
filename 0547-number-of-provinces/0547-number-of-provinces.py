class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        arr = [False] * len(isConnected[0])
        provinces = 0
        
        def dfs(i):
            for adjacent_city in range(len(isConnected)):
                if isConnected[i][adjacent_city] == 1 and not arr[adjacent_city]:
                    arr[adjacent_city] = True
                    dfs(adjacent_city)
                    
        for city in range(len(isConnected)):
            if not arr[city]:
                dfs(city)
                provinces += 1

        return provinces