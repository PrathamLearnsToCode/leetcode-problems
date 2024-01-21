class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int flag = 0;
        int maxi = 0;
        for(int i = 0;i<nums.size(); i++){
            if(nums[i]==1){
                flag = nums[i] + flag;
                maxi = max(flag,maxi);
            }
            else{
                flag = 0;
                maxi = max(flag,maxi);
                
            }
        }
        return maxi;
    }
};