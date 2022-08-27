class Solution:
    def countPoints(self, rings: str) -> int:
        d = {}
        
        for i in range(1,len(rings),2):
            j = rings[i]
            if j not in d:
                d[j]=rings[i-1]
            else:
                d[j]+=rings[i-1]
                
        print(d)
        
        ret = 0
        for i in list(d.keys()):
            if ('B' in d[i]) and ('G' in d[i]) and ('R' in d[i]):
                ret+=1
            
        return ret