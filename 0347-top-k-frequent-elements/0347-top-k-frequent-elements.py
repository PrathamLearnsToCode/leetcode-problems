class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        
        for i in nums:
            if i in countNums:
                countNums[i] += 1
                
            else:
                countNums[i] = 1
                
        sorted_elements = sorted(countNums.items(), key = lambda x:x[1], reverse = True)
        
        top_k_elements = [element for element, frequency in sorted_elements[:k]]
        
        return top_k_elements
        