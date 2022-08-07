class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        mLen = [len(i) for i in strs]
        mLen = min(mLen)
        print(mLen)
        
        f = 0
        ret = ''
        for i in range(0, mLen):
            chk = strs[0][i]
            for j in range(0, len(strs)): # traversing the rows
                if(strs[j][i] != chk):
                    f = 1
                    break
            if f == 1:
                break
            ret+=chk
            
        return ret
            
                
                
            
        