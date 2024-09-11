class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l<r:
            if s[l] == s[r]:
                char = s[l]
                while l<=r and s[l] == char:
                    l+=1
                while l<=r and s[r]==char:
                    r-=1

            else:
                break
                        
        return r - l + 1