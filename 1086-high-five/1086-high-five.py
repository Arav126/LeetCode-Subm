class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        d = {}
        
        for i in items:
            if i[0] not in d:
                d[i[0]] = [i[1]]
            else:
                d[i[0]].append(i[1])
        
        for i in list(d.keys()):
            temp = d[i]
            temp.sort()
            temp.reverse()
            d[i] = temp
            
        ret = []
        for i in list(d.keys()):
            p = d[i]
            p = p[0:5]
            avg = sum(p)/5
            
            ret.append([i,floor(avg)])
            
            
        ret.sort()
        return ret