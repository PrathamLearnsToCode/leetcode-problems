class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize-1
        summation = 0
        
        for i in range(len(nums)):
            summation += nums[i]
            
            if summation>maxi:
                maxi = summation
                
            if summation<0:
                summation = 0
                
        return maxi