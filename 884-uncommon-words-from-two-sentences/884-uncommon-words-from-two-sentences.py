class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        l1 = s1.split()
        l2 = s2.split()
        ret = []
        
        ##################
        d1,d2 = {},{}
        
        for i in l1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
                
        for i in l2:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
                
        # print(d)
        
        for i in list(d1.keys()):
            if d1[i]!=1:
                d1.pop(i)
                if i in d2:
                    d2.pop(i)
                
        for i in list(d2.keys()):
            if d2[i]!=1:
                d2.pop(i)
                if i in d1:
                    d1.pop(i)
        
        # print(d)
        
        l1 = list(d1.keys())
        l2 = list(d2.keys())
        
        ##################
        
        for i in l1:
            if i not in l2:
                ret.append(i)
                
        for i in l2:
            if i not in l1:
                ret.append(i)
                
        return ret
                