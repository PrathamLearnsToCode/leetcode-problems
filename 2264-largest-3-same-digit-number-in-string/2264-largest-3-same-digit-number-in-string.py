class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi = ""
        for i in range(len(num)-2):
            substr = num[i:i+3]
            if substr[0]==substr[1]==substr[2]:
                maxi = max(substr,maxi)
            else:
                continue
                
        return maxi
        