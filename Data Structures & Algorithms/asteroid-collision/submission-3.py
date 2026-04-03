class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            current = asteroids[i]
            # if collision
            while stack and stack[-1] > 0 and current < 0:
                # if incoming asteroid is bigger
                if stack[-1] < abs(current):
                    stack.pop()
                    continue
                
                # if same size
                elif stack[-1] == abs(current):
                    stack.pop()
                    current = 0
                    break
                
                # keep stack the same if one on stack is bigger
                else:
                    current = 0
                    break

            # append to stack if not destroyed
            if current != 0:
                stack.append(current)
            
        return stack