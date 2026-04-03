class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #iterate through temps
        #compare each element to top of stack
        #if bigger, pop elements and calculate index dist
        #if not push onto stack
        stack = []
        temps = temperatures
        res = [0] * len(temps)
        for i in range(len(temperatures)):
            #add temp to stack if it not bigger than the current end of stack
            while stack and temps[i] > stack[-1][0]:
                #pop until we reach an element that is not smaller
                pop = stack.pop()
                pop_index = pop[-1]
                dist = i - pop_index
                res[pop_index] = dist
            stack.append([temps[i], i])
        return res