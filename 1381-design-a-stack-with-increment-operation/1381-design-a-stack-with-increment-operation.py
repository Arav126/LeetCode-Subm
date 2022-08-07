class CustomStack:

    def __init__(self, maxSize: int):
        self.sz = maxSize
        self.stack = []
        self.top = None
        

    def push(self, x: int) -> None:
        if(len(self.stack) < self.sz):
            self.stack.append(x)
        

    def pop(self) -> int:
        if(len(self.stack)>0):
            j = self.stack.pop()
            # self.top = self.stack[len(self.stack)-1]
            return j
        elif len(self.stack) == 0 :
            return -1

    def increment(self, k: int, val: int) -> None:
        
        if(k >= len(self.stack)):
            for i in range(0, len(self.stack)):
                self.stack[i]+= val
        elif(k < len(self.stack)):
            for i in range(0, k): # starting from 0
                self.stack[i] += val
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)