class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> mpp;
        for(auto it:s){
            mpp[it]++;
        }
        
        for(auto ti:t){
            mpp[ti]--;
        }
        
        for(auto x:mpp){
            if(x.second!=0){
                return false;
            }
        }
        return true;
    }
};