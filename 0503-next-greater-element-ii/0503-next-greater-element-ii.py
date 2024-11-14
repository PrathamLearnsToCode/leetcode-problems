class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        result = [-1] * len(nums)
        
        n = len(nums)
        for i in range(2*n - 1, -1, -1):
            num = nums[i % n]
            while stack and stack[-1] <= num:
                stack.pop()
                        
            if i < len(nums):
                result[i] = stack[-1] if stack else -1
            
            stack.append(num)
            
        return result
        