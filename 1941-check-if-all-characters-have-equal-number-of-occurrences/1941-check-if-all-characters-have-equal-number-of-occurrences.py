class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        d ={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        chk = d[list(d.keys())[0]]
        
        for i in list(d.keys()):
            if d[i] != chk:
                return False
        return True
        