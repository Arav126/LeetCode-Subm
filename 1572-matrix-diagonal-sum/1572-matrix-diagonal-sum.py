class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = []
        
        j = len(mat)-1
        for i in range(len(mat)):
            if(i == j):
                ans.append(mat[i][i])
                j-=1
                continue
            ans.append(mat[i][i])
            ans.append(mat[i][j])
            j-=1
            
        # print(ans)
            
        return sum(ans)