class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-s for s in nums]
        heapq.heapify(minHeap)
        
        for i in range(k-1):
            heapq.heappop(minHeap)
            
        return -heapq.heappop(minHeap)
            
        