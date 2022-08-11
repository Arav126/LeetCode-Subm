class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for i in range(0, len(matrix)):
        #     j = matrix[i].index(0)
        #     return j
        
        ind = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    ind.append([i,j])
                    
        for i in range(0,len(ind)):
            for j in range(0,len(matrix[0])):
                matrix[ind[i][0]][j] = 0
                
            for j in range(0,len(matrix)):
                matrix[j][ind[i][1]] = 0