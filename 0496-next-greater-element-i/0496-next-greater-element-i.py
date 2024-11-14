class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        next_ele = {}
        for nums in reversed(nums2):
            while stack and stack[-1] < nums:
                stack.pop()
                
            next_ele[nums] = stack[-1] if stack else -1
            
            stack.append(nums)
            
        return [next_ele[nums] for nums in nums1]