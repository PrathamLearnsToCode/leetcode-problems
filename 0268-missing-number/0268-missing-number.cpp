#include<vector>
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        std::vector<int> arr(nums.size() + 1, 0);
        for(int i = 0; i<nums.size(); i++){
            arr[nums[i]] = 1;
        }
        
        for(int j = 0; j<arr.size(); j++){
            if(arr[j]==0){
                return j;
            }
        }
        
        return -1;   
    }
};