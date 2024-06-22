class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while(left<=right):
            middle = left + (right - left)//2
            
            if((middle == 0 or nums[middle]!=nums[middle-1]) and (middle==len(nums) - 1 or nums[middle]!=nums[middle+1])):
                return nums[middle]
                
            if middle%2==0:
                if(nums[middle]==nums[middle-1]):
                    right = middle - 1
                else:
                    left = middle + 1
                
            else:
                if(nums[middle+1]==nums[middle]):
                    right = middle - 1
                else:
                    left = middle + 1
                
                
        