class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li = []
        for x,y in points:
            dist = sqrt((x**2) + (y**2))
            li.append((dist,x,y))
            
        heapq.heapify(li)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(li)
            res.append((x,y))
            
        return res
        