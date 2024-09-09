class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            if i*i == num:
                return True
            if i*i>num:
                return False
        