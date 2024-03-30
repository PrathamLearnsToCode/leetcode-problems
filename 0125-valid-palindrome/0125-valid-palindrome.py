class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        
        for c in s:
            if c.isalnum():
                newstr = c.lower() + newstr
                
        return newstr == newstr[::-1]
                
                
        