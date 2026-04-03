from collections import deque

q = deque()
q.append('First item') # Enqueue
q.append('Second item') # Enqueue

print(q.popleft()) # Dequeue -> 'First item'
print(q.popleft()) # Dequeue -> 'Second item'

class MyStack:

    def __init__(self):
        self.main_q = deque()
        self.temp_q = deque()


    def push(self, x: int) -> None:
        #goal keep track of most recent element queued
        # need to be able to eject that value form my 2 queue ds
        # clear the queue into the other queue, then dequeue the last remaining elment when size is 1
        self.main_q.append(x)

    def pop(self) -> int:
        i = 0
        if len(self.main_q) == 0:
            return

        while len(self.main_q) > 1:
            self.temp_q.append(self.main_q.popleft())

        #copy temp back to main
        while len(self.temp_q) > 0:
            self.main_q.append(self.temp_q.popleft())
            
        return self.main_q.popleft()
        

        

    def top(self) -> int:
        i = 0
        if len(self.main_q) == 0:
            return

        while len(self.main_q) > 1:
            self.temp_q.append(self.main_q.popleft())

        end = self.main_q[0]
        self.temp_q.append(self.main_q.popleft())

        #copy temp back to main
        while len(self.temp_q) > 0:
            self.main_q.append(self.temp_q.popleft())
        return end
                

    def empty(self) -> bool:
        return True if len(self.main_q) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()