class Solution:
    def mySqrt(self, x: int) -> int:
        f = x**0.5
        
        f = floor(f)
        
        return f