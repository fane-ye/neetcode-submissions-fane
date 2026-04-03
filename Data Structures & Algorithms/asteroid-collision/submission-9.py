class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #iterate through asteroids
        stack = []
        for ast in asteroids:
            to_push = True

            #while stack has elements and in collision state
            while stack and ast < 0 and stack[-1] > 0:

                #if incoming is bigger, pop existing
                if abs(ast) > stack[-1]:
                    stack.pop()
                    to_push = True
                
                # if equal , pop existing
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    to_push = False
                    break

                #if incoming is smaller, to_push = False
                else:
                    to_push = False
                    break


            #load aseroid onto stack if empty
            # if was equal dont push
            # if bigger, add
            if to_push:
                stack.append(ast)


        return stack