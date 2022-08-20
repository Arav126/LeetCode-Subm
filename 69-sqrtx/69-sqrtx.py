class Solution:
    def mySqrt(self, x: int) -> int:
#         f = x**0.5
        
#         f = floor(f) # this is literally built in
        
#         return f

        # approach using binary search similar to a prev question of guessing
    
        if x < 2:
            return x
        
        
        lo = 2
        hi = x//2 #square root is always lesser than x/2
        
        while(lo<=hi):
            mi = (lo+hi)//2
            
            if mi**2 == x:
                return mi
            elif mi**2 > x: #going away
                hi = mi-1
            elif mi**2 < x: # the floor value which needs to be returned is tested and lo>hi breaks while, initially at one point both lo == hi but lo has changed, so we must return hi
                lo = mi+1
                
        # return lo # the floor value closeset to the exact square how smart
        return hi # it's actually not the lo but hi, 