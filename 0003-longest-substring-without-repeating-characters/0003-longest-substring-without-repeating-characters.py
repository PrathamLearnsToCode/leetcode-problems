class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            
            
            unique.add(s[r])
            max_len = max(max_len, r - l + 1)
            
            
        return max_len
        