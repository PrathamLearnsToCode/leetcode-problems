class Solution {
public:
    void subset(int index, int n, vector<int>& nums, vector<vector<int>> &ans, vector<int> &arr){
        if(index == n){
            ans.push_back(arr);
            return;
        }
        arr.push_back(nums[index]);
        subset(index + 1, n, nums, ans, arr);
        arr.pop_back();
        subset(index + 1, n, nums, ans, arr);        
    }
    
    
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> arr;
        int n = nums.size();
        subset(0, n, nums, ans, arr);
        return ans;
    }
};