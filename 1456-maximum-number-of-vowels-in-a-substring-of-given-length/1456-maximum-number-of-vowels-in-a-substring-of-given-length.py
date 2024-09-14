class Solution:
    def maxVowels(self, s: str, k: int) -> int:       
        l = 0
        res = 0
        vowels = "aeiou"
        count = 0
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
            if (r-l + 1)>k:
                if s[l] in vowels:
                    count -= 1
                l+=1
            res = max(res,count)
            
        return res
            