class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summation = 0

        mini = float('inf')
        for r in range(len(nums)):
            summation += nums[r]
                
            while summation >= target:
                mini = min(mini,r-l+1)
                summation -= nums[l]
                l += 1
                
            
        return mini if mini != float('inf') else 0
                