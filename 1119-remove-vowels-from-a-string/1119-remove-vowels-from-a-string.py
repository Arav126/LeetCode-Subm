class Solution:
    def removeVowels(self, s: str) -> str:
        
        l = ["a","e","i","o","u"]
        lc = [i for i in s]
        
        i=0
        while(1):
            if lc[i] in l:
                lc.pop(i)
            else:
                i+=1
                
            if i == len(lc):
                break
        
        ret = ''.join(lc)
        return ret
        