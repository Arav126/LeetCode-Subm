class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl = [i for i in s]
        tl = [i for i in t]
        
        for i in sl:
            tl.pop(tl.index(i))
            # print(tl)
            
        # print(tl)
            
        return tl[0]
        