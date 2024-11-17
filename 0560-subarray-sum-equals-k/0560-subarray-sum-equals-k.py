class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_sum = 0
        prefixSums = { 0 : 1 }
        
        for i in nums:
            current_sum += i
            diff = current_sum - k
            
            res += prefixSums.get(diff,0)
            
            prefixSums[current_sum] = 1 + prefixSums.get(current_sum,0)
            
            
        return res
            
        