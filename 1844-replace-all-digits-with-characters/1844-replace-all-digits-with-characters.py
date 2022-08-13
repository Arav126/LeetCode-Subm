class Solution:
    def replaceDigits(self, s: str) -> str:
        
        l = [i for i in s]
        for i in range(1,len(s),2):
            l[i] = self.shift(l[i-1],l[i])
            
        ret = ''.join(l)
        return ret
    
    def shift(self, c, x):
        
        integer = int(x)
        
        char = ord(c) + integer
        ret = chr(char)
        
        return ret
    
        