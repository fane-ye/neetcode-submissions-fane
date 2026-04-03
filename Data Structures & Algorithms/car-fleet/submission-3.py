class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort cars by position
        cars = list(zip(position, speed))
        cars = sorted(cars, key=lambda x:x[0], reverse=True)

        stack = []
        #then load cars onto stack
        for car in cars:
            toa = (target - car[0])/car[1] #(target-pos) / spd
            
            # if toa > fleet in front, create new fleet, push onto stack
            if not stack or toa > stack[-1]:
                stack.append(toa)
            # if toa of car being loaded is < fleet in front, join fleet, dont push
            
        return len(stack)