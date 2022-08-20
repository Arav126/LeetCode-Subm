class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        ret = []
        # c = 1
        i = 1
        while(1):
            n-=i
            if n<0:
                return i-1
            i+=1
            
            