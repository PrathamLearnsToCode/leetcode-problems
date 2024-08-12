class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in words:
            start = 0
            end = len(i) - 1
            while start<end:
                if i[start]!= i[end]:
                    break
                start += 1
                end-= 1
            else:
                return i

        return ""
        