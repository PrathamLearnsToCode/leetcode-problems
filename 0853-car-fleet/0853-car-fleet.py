class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)
        res = 0
        stack = []
        
        for pos, spd in cars:
            time = (target - pos)/spd
            if not stack or time>stack[-1]:
                stack.append(time)
                res += 1
        
        
        return res
        