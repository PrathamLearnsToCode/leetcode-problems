class Solution {
private:
    bool isAlphanumeric(char c) {
        return isalpha(c) || isdigit(c);
    }

    bool isPalin(int i, int n, vector<char>& str) {
        if (i >= n / 2) {
            return true;
        }

        if (str[i] != str[n - i - 1]) {
            return false;
        }
        return isPalin(i + 1, n, str);
    }

public:
    bool isPalindrome(string s) {
        vector<char> str;

        for (int i = 0; i < s.length(); i++) {
            if (isAlphanumeric(s[i])) {
                str.push_back(tolower(s[i]));
            }
        }
        return isPalin(0, str.size(), str);
    }
};
