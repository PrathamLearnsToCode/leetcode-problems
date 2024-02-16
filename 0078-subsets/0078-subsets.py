class Solution:
    def subseq(self, index, n, nums, ans, arr):
        if(index==n):
            ans.append(arr[:]);
            return;
        arr.append(nums[index])
        self.subseq(index+1, n, nums, ans, arr)
        arr.pop()
        self.subseq(index + 1, n, nums, ans, arr)
        
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        n = len(nums)
        self.subseq(0, n, nums, ans, arr)
        return ans;
        