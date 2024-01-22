class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int n = nums.size();
        int s = 0;
        for(int i = 0; i<n; i++){
            s = nums[i] + s;
            nums[i] = s;
        }
        return nums;
    }
};