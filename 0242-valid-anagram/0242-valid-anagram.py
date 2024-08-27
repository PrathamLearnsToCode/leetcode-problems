class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        
        for i in list(s):
            if i in countS:
                countS[i] += 1
            else:
                countS[i] = 1
                
        for j in list(t):
            if j in countT:
                countT[j] += 1
            else:
                countT[j] = 1
                
        return countS==countT
            
        