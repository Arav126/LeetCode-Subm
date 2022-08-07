class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        
        norm = []
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                # print(i, " | ", j)
                n = mat[i][j]
                norm.append(n)
                
        # print(norm)
        if(len(norm) != (r*c)):
            return mat
                
        ans = [[0 for i in range(0, c)] for j in range(0, r)]
        # print(ans)
        for i in range(0, r):
            for j in range(0, c):
                ans[i][j] = norm.pop(0)
                # print(ans)
                
        # print(ans)
        return ans
        
        
        
        