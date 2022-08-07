class Solution:
    def addDigits(self, num: int) -> int:
        
        s = str(num)
        
        sm = num
        while(len(s) != 1):
            l = [int(i) for i in str(sm)]
            sm = sum(l)
            s = str(sm)
            
        return sm
        