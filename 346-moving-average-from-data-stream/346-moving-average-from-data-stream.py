class MovingAverage:

    def __init__(self, size: int):
        self.l = []
        self.size = size
        

    def next(self, val: int) -> float:
        self.l.append(val)
        if len(self.l) > self.size :
            self.l.pop(0)
            
        avg = sum(self.l)/len(self.l)
        
        return avg
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)