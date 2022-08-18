class Solution:
    def isArmstrong(self, n: int) -> bool:
        
        if n<0:
            return False
        
        l = [int(i) for i in str(n)]
        lp = [i**len(l) for i in l]
        
        arm = sum(lp)
        
        if arm == n:
            return True
        return False
        