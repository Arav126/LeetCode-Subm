class Solution:
    def signFunc(self, j:int) -> int:
        if j > 0 :
            return 1
        elif j < 0 : 
            return -1
        else:
            return 0
        
    def arraySign(self, nums: List[int]) -> int:
        
        prod = 1
        
        for i in nums:
            prod *= i
            
        return self.signFunc(prod)
    
    
        