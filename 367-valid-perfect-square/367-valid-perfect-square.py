class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
#         x = num**0.5 # other words for a sqrt function
        
#         if(int(x)==x):
#             return True
#         else:
#             return False

        # Simple binary search with guess squared approach, this is frankly stupid
    
        if num<2: return True
        
        lo = 2
        hi = num//2
        
        while(lo<=hi):
            mi = (lo+hi)//2
            if mi**2 == num:
                return True
            elif mi**2 > num: # then u must move back
                hi = mi-1
            elif mi**2 < num:
                lo = mi+1
                
        return False
        