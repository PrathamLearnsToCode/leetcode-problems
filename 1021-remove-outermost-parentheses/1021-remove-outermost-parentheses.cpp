class Solution {
public:
    string removeOuterParentheses(string s) {
        stack<char> st;
        string ans;
        for(auto x:s){
            if(x == '('){
                if(st.size()>0){
                    ans.push_back(x);
                }
                st.push(x);
            }
            else{
                st.pop();
                if(!st.empty()){
                    ans.push_back(x);
                }
            }
        }
        return ans;
        
    }
};