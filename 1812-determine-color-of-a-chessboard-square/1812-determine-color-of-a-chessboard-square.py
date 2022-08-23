class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        d = {
            'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8
        }
        
        cord1 = d[coordinates[0]]
        cord2 = int(coordinates[1])
        
        if (cord1+cord2)%2==0:
            return False
        else:
            return True
        