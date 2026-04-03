class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
            # else:
                #merges into existing fleet
        return len(stack)  
            