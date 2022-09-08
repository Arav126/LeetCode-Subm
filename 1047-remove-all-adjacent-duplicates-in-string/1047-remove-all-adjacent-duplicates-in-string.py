class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        ret = []
        
        if len(s) == 0:
            return ret
        
        ret.append(s[0])
        if len(s) == 1:
            return ret
        
        # print(ret[-1])
        for i in range(1,len(s)):
            if len(ret)!=0 and s[i]==ret[-1]:
                ret.pop(-1)
            else:
                ret.append(s[i])
                
            # print(ret)
        
        return ''.join(ret)