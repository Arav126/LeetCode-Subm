class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        
        d = {}
        
        for i in range(0, len(items1)):
            if items1[i][0] not in d:
                d[items1[i][0]] = items1[i][1]
            else:
                d[items1[i][0]]+= items1[i][1]
                
        for i in range(0, len(items2)):
            if items2[i][0] not in d:
                d[items2[i][0]] = items2[i][1]
            else:
                d[items2[i][0]]+= items2[i][1]
                
        # d.sort()
                
        ret = [[0 for i in range(0, 2)] for j in range(0, len(d))]
        
        j = 0
        for i in sorted(d.keys()):
            ret[j][0] = i
            ret[j][1] = d.get(i)
            j+=1
        
        # for i in range(0, len(ret)):
        #     ret[i][0] = list(d.keys())[i]
        #     ret[i][1] = list(d.values())[i]
        
        return ret
                
        
                
        
        
        