class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        
        for i in arr:
            s = bin(i)
            temp = s[2:]
            temp = str(temp)
            c = temp.count("1")
            if c not in d:
                d[c]=[]
                d[c].append(i)
            else:
                d[c].append(i)
                
        print(list(d.values()))
        
        for i in list(d.keys()):
            l = d[i]
            l.sort()
            d[i] = l
            
        # print(list(d.values()))
        # sorting a dictionay with n
        
        dv = list(d.keys())
        dv.sort()
        sl = []
        for i in dv:
            sl.append(d[i])
            
        # print(sl)
            
        ret = [i for subList in sl for i in subList]
            
        return ret
            
            
        