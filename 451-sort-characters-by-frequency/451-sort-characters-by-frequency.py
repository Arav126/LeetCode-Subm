class Solution:
    def frequencySort(self, s: str) -> str:
        
        # building a dictionary
        d = {}
        l = [i for i in s]
        
        for i in l:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
                
        sv = list(d.values())
        sv.sort()
        sv.reverse()
        
        ret = ""
        
        for i in sv:
            ind = (list(d.keys()))[list(d.values()).index(i)]
            ret+= ind * i
            d.pop(ind)
            
        return ret
        
        