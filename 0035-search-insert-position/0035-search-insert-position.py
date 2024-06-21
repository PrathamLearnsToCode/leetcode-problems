class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        s = 0
        e = len(nums) - 1
        
        while(s<=e):
            middle = (s+e)//2
            
            if(target==nums[middle]):
                return middle
            elif(target>nums[middle]):
                s = middle + 1
            elif(target<nums[middle]):
                e = middle - 1
                
                
        return s
        