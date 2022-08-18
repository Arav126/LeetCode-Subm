class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        # building dict
        
        d = {}
        
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        # print(d)
        
        for i in list(d.keys()):
            if d[i]!=1:
                d.pop(i)
        
        # print(d)
        
        ret = list(d.keys())
        
        if (k-1)<len(ret):
            return ret[k-1]
        else:
            return ""