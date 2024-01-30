#include <stack>
#include <sstream>

class Solution {
public:
    string reverseWords(string s) {
        stack<string> st;
        string str = "";
        
        // Skip leading spaces
        int start = 0;
        while (start < s.length() && s[start] == ' ') {
            start++;
        }
        
        for (int i = start; i < s.length(); i++) {
            if (s[i] == ' ') {
                st.push(str);
                str = "";
                
                // Skip consecutive spaces
                while (i + 1 < s.length() && s[i + 1] == ' ') {
                    i++;
                }
            } else {
                str += s[i];
            }
        }
        
        // Handle trailing spaces
        if (!str.empty()) {
            st.push(str);
        }
        
        string ans = "";
        while (!st.empty()) {
            ans += st.top() + " ";
            st.pop();
        }
        
        // Remove the trailing space
        if (!ans.empty()) {
            ans.pop_back();
        }
        
        return ans;
    }
};
