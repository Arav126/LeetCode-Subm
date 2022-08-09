class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)
        y = bin(y)
        
        # print(x)
        # print(y)
        
        xl = [int(i) for i in x[2:]]
        yl = [int(i) for i in y[2:]]
        
        
        
        if len(xl) > len(yl):
            diff = len(xl)-len(yl)
            for i in range(0, diff) : yl.insert(0,0)
            
        elif(len(xl) < len(yl)):
            diff = len(yl)-len(xl)
            for i in range(0, diff) : xl.insert(0,0)
        
        # print(xl)
        c = 0
        for i in range(0, len(xl)):
            if xl[i]!=yl[i]:
                c+=1
                
        return c