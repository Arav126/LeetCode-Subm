class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        x = num**0.5 # other words for a sqrt function
        
        if(int(x)==x):
            return True
        else:
            return False
        