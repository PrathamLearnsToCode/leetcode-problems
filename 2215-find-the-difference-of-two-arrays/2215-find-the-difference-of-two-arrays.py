class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1set = set(nums1)
        res2set = set(nums2)
        
        res1 = set()
        res2 = set()
        
        for i in nums1:
            if i not in res2set:
                res1.add(i)
                
        for i in nums2:
            if i not in res1set:
                res2.add(i)
                
        return[list(res1), list(res2)]