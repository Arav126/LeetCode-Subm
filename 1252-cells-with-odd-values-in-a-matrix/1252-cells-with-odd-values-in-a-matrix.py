class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        mat = [[0 for j in range(n)] for i in range(m)]
        # print(mat)
        for i in indices:
            for j in range(m):
                mat[j][i[1]]+=1
                
            for j in range(n):
                mat[i[0]][j]+=1
                
        # print(mat)
        ret = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]%2==1:
                    ret+=1
                    
        return ret
            
        