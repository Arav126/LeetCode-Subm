class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        # building a dict
        
        d = {}
        
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        print(d)
        
        it = list(d.keys())
        it.sort()
        it.reverse()
        for i in it:
            if i == d[i]:
                return i
            
        return -1
        