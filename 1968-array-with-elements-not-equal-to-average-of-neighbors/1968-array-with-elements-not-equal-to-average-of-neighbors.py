class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = []
        
        while left<= right:
            result.append(nums[left])
            left += 1
            
            if left<=right:
                result.append(nums[right])
                right -= 1
                
        return result
        