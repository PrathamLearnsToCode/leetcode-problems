class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int n = nums.size();
        while(low<=high){
            int middle = (high+low)/2;
            if(nums[middle]>=target){
                n = middle;
                high = middle - 1;
            }
            else{
                low = middle + 1;
            }
        }
        return n;
    }
};