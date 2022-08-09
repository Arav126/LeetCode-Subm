class Solution:
    def fib(self, n: int) -> int:
        
        ret = self.fibRec(n)
        return ret 
    
    def fibRec(self, n: int):
        if n==0:
            return 0
        if n==1:
            return 1
        
        return self.fibRec(n-1)+self.fibRec(n-2)
            
        
        