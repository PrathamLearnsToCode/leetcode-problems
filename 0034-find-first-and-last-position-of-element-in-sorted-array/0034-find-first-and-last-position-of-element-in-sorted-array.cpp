class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n=nums.size();
        int l=0;
        int r=n-1;
        int start=-1,end=-1;
        int mid;
        while(l<=r){
            mid=l+(r-l)/2;
            if(nums[mid]>target){
                r=mid-1;
            }else if(nums[mid]==target){
                start=mid;
                r=mid-1;
            }else{
                l=mid+1;
            }
        }
        l=0;
        r=n-1;
        while(l<=r){
            mid=l+(r-l)/2;
            if(nums[mid]>target){
                r=mid-1;
            }else if(nums[mid]==target){
                end=mid;
                l=mid+1;
            }else{
                l=mid+1;
            }
        }
        return {start,end};
        
        
    }
};