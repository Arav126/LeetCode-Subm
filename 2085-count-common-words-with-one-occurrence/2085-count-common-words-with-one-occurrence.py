class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
                # building dict
        
        d1,d2 = {},{}
        
        for i in words1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
                
        for i in words2:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
                
        # print(d)
        
        for i in list(d1.keys()):
            if d1[i]!=1:
                d1.pop(i)
                
        for i in list(d2.keys()):
            if d2[i]!=1:
                d2.pop(i)
        
        # print(d)
        
        ret = 0 
        
        for i in d1:
            if i in d2:
                ret+=1
                
        return ret
        