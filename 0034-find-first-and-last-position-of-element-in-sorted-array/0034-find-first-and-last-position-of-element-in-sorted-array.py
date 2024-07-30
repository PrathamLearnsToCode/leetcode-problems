class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      
      def findfirst(nums, target):
        l, r = 0, len(nums) - 1
        first = -1
        while l <= r:
          middle = (l + r) // 2
          if nums[middle] == target:
              first = middle
              r = middle - 1
          elif nums[middle] < target:
              l = middle + 1
          else:
              r = middle - 1
        return first
        
      def findLast(nums, target):
        l, r = 0, len(nums) - 1
        last = -1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                last = middle
                l = middle + 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return last
      
      first = findfirst(nums, target)
      last = findLast(nums, target)
        
      return [first, last] if first != -1 else [-1, -1]
        