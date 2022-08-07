class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        
        if numRows == 0:
            return ans
        
        if numRows == 1:
            ans.append([1])
            return ans
        
        
        ans.append([1])
        l = []
        for i in range(2, numRows+1):
            length = i
            l = [0] * length
            l[0],l[-1] = 1,1
            
            for j in range(1, length-1):
                
                l[j] = ans[i-2][j-1] + ans[i-2][j]
                
            # print(l)
            ans.append(l)
            # print(ans)
            
        return ans
            
            
            
            
        