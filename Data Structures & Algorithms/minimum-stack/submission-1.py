class MinStack:

    def __init__(self):
        self.stack = []
        self.tracking_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.updateMin(val)
        

    def pop(self) -> None:
        if self.stack.pop() == self.getMin():
            self.tracking_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        if self.tracking_stack: 
            return self.tracking_stack[-1]

    def updateMin(self, num) -> int:
        if not self.tracking_stack or num <= self.tracking_stack[-1]:
            self.tracking_stack.append(num)
        return
        
